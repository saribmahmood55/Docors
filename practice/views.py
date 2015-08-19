from practice.models import *
from patients.models import Patient
from reviews.models import Review
from utility import *
from practitioner.models import Practitioner
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

from docors.forms import advanced_form, speciality_form

def search_advanced(request):
    if request.method == "POST":
        form = advanced_form(request.POST)
        if form.is_valid():
            spec = form.cleaned_data['spec_adv']
            dist = form.cleaned_data['radius']
            lat = form.cleaned_data['lat']
            lon = form.cleaned_data['lon']
            day = form.cleaned_data['day']
            request.session['day'] = day
            request.session['lat'] = lat
            request.session['lon'] = lon
            spec = Specialization.objects.get(pk=spec)
            return HttpResponseRedirect(reverse('results_advanced', kwargs={'speciality':spec.slug,'dist':dist}))
    return HttpResponseRedirect(reverse('index'))

def results_advanced(request, speciality, dist):
    data = dict()
    day = request.session['day']
    lat = request.session['lat']
    lon = request.session['lon']
    data['practice'] = Practice.practice_objects.adv_practice_lookup(speciality, dist, lat, lon, day)
    data['ob'] = Specialization.objects.get(slug=speciality)
    data['results_count'] = len(data['practice'])
    data['results_header'] = data['ob'].human_name + " within " + str(dist) + " KM radius"
    return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

def search_specialty(request):
    if request.method == "GET":
        form = speciality_form(request.GET)
        if form.is_valid():
            spec_pk = request.GET.get('spec', '')
            speciality = Specialization.objects.get(pk=spec_pk).slug
            area_pk = request.GET.get('area', '')
            area = Area.objects.get(pk=area_pk).slug
            return HttpResponseRedirect(reverse('results_specialty', kwargs={'speciality' : speciality, 'area': area}))
    return HttpResponseRedirect(reverse('index'))

#recent Searches
def results_specialty(request, speciality, area):
    data = {'area': area, 'spec': speciality}
    if request.method == "GET":
        try:
            data['practice'] = Practice.practice_objects.practice_recentlookups(area, speciality)
            data['ob'] = Specialization.objects.get(slug=speciality)
            data['results_count'] = len(data['practice'])
            data['results_header'] = speciality + " near " + Area.area_objects.get_full_name(area)
        except Practice.DoesNotExist:
            raise Http404
    return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

# single practitioner details
def practitioner(request, slug):
    data = {'own_profile':True}
    if request.method == "GET":
        if request.user.is_authenticated():
            try:
                data['patient'] = Patient.patient_objects.patient_details(request.user)
                favourite_practitioner = data['patient'].favt_practitioner.all().filter(slug=slug)
                if favourite_practitioner.exists():
                    data['favourite'] = True
                else:
                    data['favourite'] = False
            except Patient.DoesNotExist:
                pass

            try:
                practitioner = request.user.practitioner
                if practitioner.slug == slug:
                    data['own_profile'] = True
            except Practitioner.DoesNotExist:
                pass
        else:
            data['patient'] = None
        try:
            data['practitioner'] = Practitioner.prac_objects.practitioner_slug(slug)
            data['practice'] = Practice.practice_objects.practice_detail(slug)
            data['practice_name'] = data['practice'].distinct('practice_location')
            data['reviews'] = Review.review_objects.practitioner_reviews(slug)
            data['pract_avg_review'] = get_review_details(data['reviews'])
        except Practitioner.DoesNotExist:
            raise Http404
    return render_to_response('practitioner/practitioner.html', {'data': data, 'practice_count':len(data['practice'])}, context_instance=RequestContext(request))

def get_areas_ajax(request):
    data = {}
    if request.is_ajax():
        if request.method == "GET":
            city = request.GET.get('city','');
            if not request.GET.get('header_city',None):
                data['areas'] = ["<option value='"+str(a.id)+"'>"+str(a)+"</option>" for a in Area.objects.filter(city=City.objects.get(pk=city))]
            else:
                data['areas'] = [a.name for a in Area.objects.filter(city=City.objects.get(slug=city))]
            return HttpResponse(json.dumps(data),content_type="application/json")
