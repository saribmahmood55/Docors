from patients.models import Patient
from reviews.models import *
from practitioner.models import *
from utility import *
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import json

#
def favourite(request, slug):
	like = {}
	if request.user.is_authenticated():
		user = request.user
		like['status_'] = favourite(user, slug)
		if request.is_ajax():
			print 'hi'
			return HttpResponse(json.dumps(like), content_type="application/json")

#
def patient(request):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == 'GET':
		if data['user']:
			try:
				data['patient'] = Patient.patient_objects.patient_details(data['user'])
				data['reviews'] = Review.review_objects.patient_reviews(data['user'])
				specialities = Specialization.objects.order_by('name')
				#specialities = specialities.exclude(data['patient'].interested_specialities)
				data['specialities'] = specialities
			except Patient.DoesNotExist:
				raise Http404
		else:
			data['user'] = None
	if request.method == 'POST':
		if request.user.is_authenticated():
			patientDetails, like, = {}, {}
			slug = request.POST.get('slug', None)
			patientDetails['user'] = data['user']
			patientDetails['fname'] = request.POST.get('fname', None)
			patientDetails['lname'] = request.POST.get('lname', None)
			patientDetails['number'] = request.POST.get('number', None)
			patientDetails['age'] = request.POST.get('age', None)
			patientDetails['gender'] = request.POST.get('gender', None)
			patientDetails['fname'] and patientDetails['lname']
			updatePatientDetails(patientDetails)
			data['patient'] = Patient.patient_objects.patient_details(data['user'])
			print "user info updated."
			data['reviews'] = Review.review_objects.patient_reviews(data['user'])
		else:
			data['patient'] = None
	return render_to_response('patients/profile.html', {'data': data}, context_instance=RequestContext(request))