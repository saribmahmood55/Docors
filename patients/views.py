from patients.models import Patient
from patients.serializers import PatientSerializer
from rest_framework import generics
from reviews.models import *
from utility import *
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from registration.signals import user_registered
from django.contrib.auth.views import login
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import json

def subscribe(request):
	slug = None
	if request.method == 'POST':
		data = {}
		slug = request.POST.get('slug', None)
		email = request.POST.get('email', None)
		cell_number = request.POST.get('phone', None)
		data['msg'] = newSubscription(slug, email, cell_number)
		if request.is_ajax():
			return HttpResponse(json.dumps(data), content_type="application/json")
	return HttpResponseRedirect(reverse('practitioner', kwargs={'slug': slug}))

def educate(request):
	data = {}
	if request.method == 'GET':
		return render_to_response('patients/educate.html', {'data': data}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def profile(request):
	data = {}
	user = request.user
	if request.method == 'GET':
		try:
			data['patient'] = Patient.patient_objects.patient_details(user)
		except Patient.DoesNotExist:
			raise Http404

	elif request.method == 'POST':
		patientDetails = {}
		patientDetails['user'] = user
		patientDetails['fname'] = request.POST.get('firstname', None)
		patientDetails['lname'] = request.POST.get('lastname', None)
		patientDetails['number'] = request.POST.get('cell_number', None)
		patientDetails['age'] = request.POST.get('age_group', None)
		patientDetails['gender'] = request.POST.get('gender', None)
		updatePatientDetails(patientDetails)
		data['patient'] = Patient.patient_objects.patient_details(user)

	return render_to_response('patients/profile.html', {'data': data}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def acc_preferences(request):
	data = {}
	user = request.user
	if request.method == "POST":
		type_ = request.POST.get('type_', None)

		if type_ == "change_email":
			new_email = request.POST.get('new_email', None)
			curr_password = request.POST.get('password', None)
			u = authenticate(username=user.username, password=curr_password)
			if u is not None:
				if u.is_active:
					pass
		elif type_ == "change_password":
			curr_email = request.user.email
			curr_password = request.POST.get('currentpassword', None)
			new_password = request.POST.get('password1', None)
			u = authenticate(username=user.username, password=curr_password)
			if u is not None:
				data['alert'] = 'Password successfully changed.'
				if u.is_active:
					u.set_password(new_password)
					u.save()
					return HttpResponseRedirect(reverse('auth_login'))
			else:
				data['alert'] = 'Unable to change password. Please check your credentials'
		elif type_ == "change_preferences":
			pass

	return render_to_response('patients/acc_preferences.html', {'data': data}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def dashboard_specialities(request):
	data = {}
	user = request.user
	if request.method == "GET":
		patient = Patient.patient_objects.patient_details(user)
		data['int_specialities'] = patient.interested_specialities.all()
		data['ex_specialities'] = excludedSpecialities(patient)
	elif request.method == "POST":
		type_ = request.POST.get('type_', None)

		if type_ == "remove":
			spec_list = request.POST.getlist('int_selector', None)
			for spec_slug in spec_list:
				interestedSpecRemove(user, spec_slug)
		elif type_ == "add":
			spec_list = request.POST.getlist('ex_selector', None)
			for spec_slug in spec_list:
				interestedSpecAdd(user, spec_slug)

		patient = Patient.patient_objects.patient_details(user)
		data['int_specialities'] = patient.interested_specialities.all()
		data['ex_specialities'] = excludedSpecialities(patient)

	return render_to_response('patients/interested_specialities.html', {'data': data}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def patient(request):
	data = {}
	user = request.user
	if request.method == 'GET':
		try:
			data['patient'] = Patient.patient_objects.patient_details(user)
			data['reviews'] = Review.review_objects.patient_reviews(user)
			data['excluded_specialties'] = excludedSpecialities(data['patient'])
		except Patient.DoesNotExist:
			raise Http404
	elif request.method == 'POST':
		if request.user.is_authenticated():
			patientDetails, response, type_ = {}, {}, None
			type_ = request.POST.get('type_', None)
			if type_ == "updatePatient":
				patientDetails['user'] = user
				patientDetails['fname'] = request.POST.get('fname', None)
				patientDetails['lname'] = request.POST.get('lname', None)
				patientDetails['number'] = request.POST.get('number', None)
				patientDetails['age'] = request.POST.get('age', None)
				patientDetails['gender'] = request.POST.get('gender', None)
				updatePatientDetails(patientDetails)
				data['patient'] = Patient.patient_objects.patient_details(user)
				print "user info updated."
				data['reviews'] = Review.review_objects.patient_reviews(user)
			elif type_ == "deleteReview":
				review_id = request.POST.get('id', None)
				response['status_'] = deleteReview(review_id)
				return HttpResponse(json.dumps(response), content_type="application/json")
			elif type_ == "deletePrac":
				slug = request.POST.get('prac_slug')
				patient = Patient.patient_objects.patient_details(user)
				response['status_'] = deleteFavtPrac(patient, slug)
				return HttpResponse(json.dumps(response), content_type="application/json")
			elif type_ == "updatereview":
				review_id = request.POST.get('review_id')
				review_text = request.POST.get('review_text')
				response['status_'] = updateReview(review_id, review_text)
				return HttpResponse(json.dumps(response), content_type="application/json")
			elif type_ == "favourite":
				slug = request.POST.get('favt_slug', '')
				user = request.user
				response['status_'] = favourite(user, slug)
				return HttpResponse(json.dumps(response), content_type="application/json")
		else:
			data['patient'] = None
	return render_to_response('patients/profile.html', {'data': data}, context_instance=RequestContext(request))

def favt_pract(request):
	slug = request.GET.get('slug','')
	resp = favourite(request.user,slug)
	return HttpResponse(json.dumps(resp), content_type="application/json")

@receiver(user_signed_up)
def set_patient(sender, **kwargs):
	user = kwargs.pop('user')
	facebook_extra_data = user.socialaccount_set.filter(provider='facebook')
	google_extra_data = user.socialaccount_set.filter(provider='google')

	p = Patient()
	p.user = user
	
	if facebook_extra_data:
		facebook_data = facebook_extra_data[0].extra_data
		if facebook_data['gender']:
			gender = facebook_data['gender'][0].capitalize()
			p.gender = gender
	elif google_extra_data:
		google_data = google_extra_data[0].extra_data
		if google_data['gender']:
			gender = google_data['gender'][0].capitalize()
			p.gender = gender

	p.save()

@receiver(user_registered)
def create_patient(sender, user, request, **kwargs):
	p = Patient(user=user)
	p.save()

	user.first_name = request.POST['firstname']
	user.last_name = request.POST['lastname']
	user.save()