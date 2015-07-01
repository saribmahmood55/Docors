from practice.models import *
from practice.serializers import PracticeSerializer, CitySerializer, CheckupFeeSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from patients.models import Patient
from reviews.models import Review
from utility import *
from practitioner.models import Practitioner, Condition, Procedure
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json


def practice(request, practice_slug, practitioner_slug):
	if request.method == "GET":
		Timing = PracticeTiming.pt_objects.practice_timings(practice_slug, practitioner_slug)
	return render_to_response('practitioner/clinictimings.html', {'Timing': Timing}, context_instance=RequestContext(request))


#Search by Name
def practitioner_name(request):
	data = {}
	if request.method == "GET":
		name = str(request.GET.get('name', ''))
		print name
		try:
			data['practice'] = Practice.practice_objects.practitioner_name(name)
		except Practice.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

#get all hospitals
def practice_hospitals(request):
	hospital_options = '<select id="id_practice_name" name="practice_name" class="form-control" onchange="change_hospital_name()"><option value="" disabled selected>Please Select from the list</option>'
	q = Practice.objects.filter(practice_type='H')
	for single_row in q:
		hospital_options = hospital_options + '<option value="' + single_row.practice_location.slug + '">' + single_row.practice_location.name + '</option>'
	hospital_options = hospital_options + '<option value="other">Other</option></select>'
	return HttpResponse(json.dumps(hospital_options),content_type="application/json")


#handle search request
def practitoners(request):
	data = {}
	if request.method == "GET":
		area = str(request.GET.get('area', ''))
		spec = str(request.GET.get('spec', ''))
		dist = int(request.GET.get('dist', 0))
		lon = request.GET.get('lon', '')
		lat = request.GET.get('lat', '')
		name = str(request.GET.get('name', ''))
		day = str(request.GET.get('day', ''))
		wait = int(request.GET.get('wait', 0))
		data['spec'] = spec
		data['area'] = area
		if lon == '' and lat == '':
			return HttpResponseRedirect(reverse('recentSearch', kwargs={'speciality': spec, 'area': area}))
		#Search Request
		try:
			data['practice'] = Practice.practice_objects.practice_lookup(area, spec, dist, lon, lat, name, day, wait)
			updateRecentSearches(area, spec)
		except Practice.DoesNotExist:
			raise Http404

	return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

def speciality_suggestions(request):
	data = {}
	if request.method == "GET":
		return HttpResponseRedirect(reverse('recentSearch', kwargs={'speciality': Specialization.spec_objects.spec_human_name(str(request.GET.get('spec', ''))).slug, 'area': Area.area_objects.area_name(str(request.GET.get('area', '') if request.GET.get('area','') != '' else 'Other')).slug}))

def get_areas(request):
	data = {}
	if request.is_ajax():
		if request.method == "GET":
			city = request.GET.get('city','');
			data['areas'] = ["<option value='"+str(a.id)+"'>"+str(a)+"</option>" for a in Area.objects.filter(city=City.objects.get(pk=city))]
			return HttpResponse(json.dumps(data),content_type="application/json")

def get_initial_reg(request):
	data = {}
	if request.is_ajax():
		if request.method == "GET":
			speciality = request.GET.get('speciality','')
			city = request.GET.get('city','')
			data['conditions'] = ["<option value='"+str(c.id)+"'>"+str(c)+"</option>" for c in Condition.objects.filter(specialization=Specialization.objects.get(pk=speciality))]
			data['procedures'] = ["<option value='"+str(p.id)+"'>"+str(p)+"</option>" for p in Procedure.objects.filter(specialization=Specialization.objects.get(pk=speciality))]
			data['areas'] = ["<option value='"+str(a.id)+"'>"+str(a)+"</option>" for a in Area.objects.filter(city=City.objects.get(pk=city))]
			return HttpResponse(json.dumps(data),content_type="application/json")


#recent Searches
def recentSearch(request, speciality, area):
	data = {'area': area, 'spec': speciality}
	if request.method == "GET":
		try:
			data['practice'] = Practice.practice_objects.practice_recentlookups(area, speciality)
			data['ob'] = Specialization.objects.get(slug=speciality)
			data['results_count'] = len(data['practice'])
			data['results_header'] = speciality + " near " + Area.area_objects.get_full_name(area)
			#updateRecentSearches(city, speciality)
		except Practice.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

# single practitioner details
def practitioner(request, slug):
	data = {}
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
		else:
			data['patient'] = None
		try:
			data['practitioner'] = Practitioner.prac_objects.practitioner_slug(slug)
			data['practice'] = Practice.practice_objects.practice_detail(slug)
			data['practice_name'] = data['practice'].distinct('practice_location')
			print data['practice_name']
			data['reviews'] = Review.review_objects.practitioner_reviews(slug)
			data['pract_avg_review'] = get_review_details(data['reviews'])
		except Practitioner.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/practitioner.html', {'data': data,'n':xrange(5)}, context_instance=RequestContext(request))
