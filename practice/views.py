from practice.models import *
from practice.serializers import PracticeSerializer, CitySerializer, CheckupFeeSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
from patients.models import Patient
from reviews.models import Review
from utility import *
from practitioner.models import Practitioner
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

class PracticeList(generics.ListCreateAPIView):
	queryset = Practice.objects.all()
	serializer_class = PracticeSerializer

class PracticeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Practice.objects.all()
	serializer_class = PracticeSerializer

class CityList(generics.ListCreateAPIView):
	queryset = City.objects.all()
	serializer_class = CitySerializer

class CityDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = City.objects.all()
	serializer_class = CitySerializer

class CheckupFeeList(generics.ListCreateAPIView):
	queryset = CheckupFee.objects.all()
	serializer_class = CheckupFeeSerializer

class CheckupFeeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CheckupFee.objects.all()
	serializer_class = CheckupFeeSerializer

class PracticeTypeList(APIView):
	def get(self, request, format=None):
		practice_types = [
			{"P":"Private Clinic/Residence"}, 
			{"H":"Hospital"}, 
			{"M":"Medical Complex"}
		]
		return Response(practice_types)

def practice(request, practice_slug, practitioner_slug):
	if request.method == "GET":
		Timing = PracticeTiming.pt_objects.practice_timings(practice_slug, practitioner_slug)
	return render_to_response('practitioner/clinictimings.html', {'Timing': Timing}, context_instance=RequestContext(request))


#Search by Name
def practitioner_name(request):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
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
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == "GET":
		city = str(request.GET.get('city', ''))
		spec = str(request.GET.get('spec', ''))
		dist = int(request.GET.get('dist', 0))
		lon = request.GET.get('lon', '')
		lat = request.GET.get('lat', '')
		name = str(request.GET.get('name', ''))
		day = str(request.GET.get('day', ''))
		wait = int(request.GET.get('wait', 0))
		data['spec'] = spec
		data['city'] = city
		if lon == '' and lat == '':
			return HttpResponseRedirect(reverse('recentSearch', kwargs={'speciality': spec, 'city': city}))
		#Search Request
		try:
			data['practice'] = Practice.practice_objects.practice_lookup(city, spec, dist, lon, lat, name, day, wait)
			updateRecentSearches(city, spec)
		except Practice.DoesNotExist:
			raise Http404

	return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))


#recent Searches
def recentSearch(request, speciality, city):
	data = {'city': city, 'spec': speciality}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == "GET":
		try:
			data['practice'] = Practice.practice_objects.practice_recentlookups(city, speciality)
			updateRecentSearches(city, speciality)
		except Practice.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

# single practitioner details
def practitioner(request, slug):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == "GET":
		if request.user.is_authenticated():
			data['patient'] = Patient.patient_objects.patient_details(data['user'])
			favourite_practitioner = data['patient'].favt_practitioner.all().filter(slug=slug)
			if favourite_practitioner.exists():
				data['favourite'] = True
			else:
				data['favourite'] = False
		else:
			data['patient'] = None
		try:
			data['practitioner'] = Practitioner.prac_objects.practitioner_slug(slug)
			data['practice'] = Practice.practice_objects.practice_detail(slug)
			data['practice_name'] = data['practice'].distinct('practice_location')
			data['reviews'] = Review.review_objects.practitioner_reviews(slug)
		except Practitioner.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/practitioner.html', {'data': data}, context_instance=RequestContext(request))
