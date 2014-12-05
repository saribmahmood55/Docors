from practitioner.models import *
from patients.models import Patient
from reviews.models import Review
from practice.models import *
from utility import *
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.core.mail import send_mail
from practitioner.form import PractitionerForm
import json

#home page
def index(request):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == "GET":
		try:
			data['specialities'] = Specialization.objects.order_by('human_name')
			data['cities'] = City.objects.order_by('pk')
		except Specialization.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/index.html', {'data': data}, context_instance=RequestContext(request))


#advance search
def adv(request):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == "GET":
		try:
			data['specialities'] = Specialization.objects.order_by('human_name')
			data['cities'] = City.objects.order_by('pk')
		except Specialization.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/advance.html', {'data': data}, context_instance=RequestContext(request))	


def registration(request):
	if request.method == 'POST':
		practitioner_form = PractitionerForm(request.POST)
		if practitioner_form.is_valid():
			#practitioner
			practitioner_name = request.POST.get('practitioner_name', '')
			email = request.POST.get('email', '')
			credentials = request.POST.get('credentials', '')
			achievements = request.POST.get('achievements', '')
			experience = request.POST.get('experience', '')
			message = request.POST.get('message', '')
			spec = request.POST.get('specialities', '')
			# Create practitioner
			practitioner = Practitioner()
			practitioner.name = name
			practitioner.email = email
			practitioner.credentials = credentials
			practitioner.achievements = achievements
			practitioner.experience = experience
			practitioner.message = message
			practitioner.status = False
			speciality = Specialization.objects.get(pk=spec)
			practitioner.specialities.add(speciality)
			practitioner.save()
			#PracticeLocation
			practice_name = request.POST.get('practice_name', '')
			address = request.POST.get('address', '')
			city = request.POST.get('city', '')
			lon = request.POST.get('lon', '')
			lat = request.POST.get('lat', '')
			#create PracticeLocation
			practice_location = PracticeLocation()
			practice_location.name = practice_name
			practice_location.address = address
			practice_location.city_id = city
			practice_location.lon = lon
			practice_location.lat = lat
			practice_location.save()
			#Practice
			practice_type = request.POST.get('practice_type', '')
			contact_number = request.POST.get('contact_number', '')
			checkup_fee = request.POST.get('checkup_fee', '')
			services = request.POST.get('services', '')
			appointment = request.POST.get('appointment', '')
			#Create Practice
			practice = Practice()
			practice.practice_type = practice_type
			practice.practice_location = practice_location
			practice.practitioner = practitioner
			practice.contact_number = contact_number
			practice.checkup_fee = checkup_fee
			practice.services = services
			practice.appointments_only = appointment
			practice.save()
			#PracticeTiming
			day_from = request.POST.get('day_from', '')
			day_to = request.POST.get('day_to', '')
			start_time = request.POST.get('start_time', '')
			end_time = request.POST.get('end_time', '')
			#Create PracticeTiming
			pt = PracticeTiming()
			pt.practitioner = practitioner
			pt.practice = practice
			pt.day = day_from
			pt.start_time
			pt.end_time
			pt.save
	else:
		practitioner_form = PractitionerForm()
	return render_to_response('practitioner/registration.html', {'form': practitioner_form}, context_instance=RequestContext(request))
















