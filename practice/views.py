from django.shortcuts import render
from patients.models import Patient
from reviews.models import Review
from practice.models import *
from practitioner.models import Practitioner
from django.http import Http404
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext

def practice(request, practice_slug, practitioner_slug):
	if request.method == "GET":
		Timing = PracticeTiming.pt_objects.practice_timings(practice_slug, practitioner_slug)
	return render_to_response('practitioner/clinictimings.html', {'Timing': Timing}, context_instance=RequestContext(request))


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
		#Search Request
		try:
			data['practice'] = Practice.practice_objects.practice_lookup(city, spec, dist, lon, lat, name, day, wait)
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