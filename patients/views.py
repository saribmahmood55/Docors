from patients.models import Patient
from reviews.models import *
from utility import *
from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import json


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
				data['excluded_specialties'] = excludedSpecialities(data['patient'])
			except Patient.DoesNotExist:
				raise Http404
		else:
			data['user'] = None
	if request.method == 'POST':
		if request.user.is_authenticated():
			patientDetails, response, type_ = {}, {}, None
			type_ = request.POST.get('type_', None)
			if type_ == "updatePatient":
				patientDetails['user'] = data['user']
				patientDetails['fname'] = request.POST.get('fname', None)
				patientDetails['lname'] = request.POST.get('lname', None)
				patientDetails['number'] = request.POST.get('number', None)
				patientDetails['age'] = request.POST.get('age', None)
				patientDetails['gender'] = request.POST.get('gender', None)
				updatePatientDetails(patientDetails)
				data['patient'] = Patient.patient_objects.patient_details(data['user'])
				print "user info updated."
				data['reviews'] = Review.review_objects.patient_reviews(data['user'])
			elif type_ == "deleteReview":
				review_id = request.POST.get('id', None)
				response['status_'] = deleteReview(review_id)
				return HttpResponse(json.dumps(response), content_type="application/json")
			elif type_ == "deletePrac":
				slug = request.POST.get('prac_slug')
				patient = Patient.patient_objects.patient_details(data['user'])
				response['status_'] = deleteFavtPrac(patient, slug)
				return HttpResponse(json.dumps(response), content_type="application/json")
			elif type_ == "favourite":
				slug = request.POST.get('favt_slug', None)
				user = request.user
				response['status_'] = favourite(user, slug)
				return HttpResponse(json.dumps(response), content_type="application/json")
		else:
			data['patient'] = None
	return render_to_response('patients/profile.html', {'data': data}, context_instance=RequestContext(request))