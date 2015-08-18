from patients.models import Patient
from patients.forms import InterestedSpecForm
from django.forms.models import modelform_factory
from practitioner.models import Practitioner
from reviews.models import *
from utility import *
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='/accounts/login/')
def physican_patient(request):
    if request.is_ajax():
        data = dict()
        if request.method == "GET":
            slug = request.GET.get('slug','')
            request_type = request.GET.get('type','delete')
            if request_type == "delete":
                data['response'] = Patient.patient_objects.remove_physican(request.user.email,Practitioner.objects.get(slug=slug))
            return HttpResponse(json.dumps(data), content_type="application/json")
    elif request.method == "GET":
        favt_practitioner = Patient.objects.get(email=request.user.email).favt_practitioner
        print favt_practitioner.all()
        return render_to_response('patients/favt_pract.html', {'favt_practitioner': favt_practitioner}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def profile_patient(request):
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

def subscribe_patient(request):
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

def educate_patient(request):
    data = {}
    if request.method == 'GET':
        return render_to_response('patients/educate.html', {'data': data}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def preferences_patient(request):
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
def specialities_patient(request):
    data = {}
    user = request.user
    if request.method == "GET":
        interestedSpecform = InterestedSpecForm(instance=request.user.patient)
    elif request.method == "POST":
        interestedSpecform = InterestedSpecForm(request.POST, instance=request.user.patient)
        if interestedSpecform.is_valid():
            interestedSpecform.save()
    patient = Patient.patient_objects.patient_details(user)
    data['int_specialities'] = patient.interested_specialities.all()

    return render_to_response('patients/interested_specialities.html', {'data': data, 'form':interestedSpecform}, context_instance=RequestContext(request))

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
