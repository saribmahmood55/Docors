from practitioner.models import *
from patients.models import Patient
from reviews.models import Review
from utility import *
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.template import RequestContext
from django.core.mail import send_mail
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
			data['specialities'] = Specialization.objects.order_by('slug')
			data['cities'] = City.objects.order_by('pk')
		except Specialization.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/index.html', {'data': data}, context_instance=RequestContext(request))


def practise(request, practise_slug, practitioner_slug):
	if request.method == "GET":
		Timing = PractiseTiming.pt_objects.practise_timings(practise_slug,practitioner_slug)
	return render_to_response('practitioner/clinictimings.html', {'Timing': Timing}, context_instance=RequestContext(request))


#handle search request
def practitoners(request):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == "GET":
		city = request.GET.get('city', '')
		name = request.GET.get('name', '')
		speciality = request.GET.get('spec', '')
		experience = request.GET.get('exp', '')
		day = request.GET.get('day', '')
	try:
		data['practise'] = Practise.practise_objects.practise_details(city, name, speciality, experience, day)
	except Practise.DoesNotExist:
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
			data['practise'] = Practise.practise_objects.practise_detail(slug)
			data['practise_name'] = data['practise'].distinct('practise_location')
			#data['practise_timing'] = clinic_timings_dic(data['practise_name'])
			data['reviews'] = Review.review_objects.practitioner_reviews(slug)
		except Practitioner.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/practitioner.html', {'data': data}, context_instance=RequestContext(request))


def update(request):
	if request.method == "POST":
		type_ = request.POST.get('type_', None)
		if type_ == "GeoLocation":
			reply = {}
			practitioner = request.POST.get('name', '')
			practise = request.POST.get('practise', '')
			lat = request.POST.get('lat', '')
			lon = request.POST.get('lon', '')
			print "doc: %s , loc: %s , lat: %s, lon: %s" % (practitioner, practise, lat, lon)
			body = "Practitioner Name: "+practitioner+"\nPractise: "+practise+"\nLatitude: "+lat+"\nLongitude: "+lon
			Email(practitioner, body)
			reply['Status'] = True
			return HttpResponse(json.dumps(reply), content_type="application/json")


def registration(request):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == "GET":
		return render_to_response('practitioner/registration.html', {'data': data}, context_instance=RequestContext(request))
	if request.method == "POST":
		email, practitioner_name = None, None
		practitioner_name = request.POST.get('practitioner_name', '')
		email = request.POST.get('email', '')
		credentials = request.POST.get('credentials', '')
		achievements = request.POST.get('achievements', '')
		experience = request.POST.get('experience', '')
		speciality = request.POST.get('speciality', '')
		#Clinic Details 1
		clinic_type1 = request.POST.get('clinic-type1', '')
		clinicName = request.POST.get('clinicName', '')
		address = request.POST.get('address', '')
		city = request.POST.get('city', '')
		number = request.POST.get('number', '')
		fee = request.POST.get('fee', '')
		services = request.POST.get('services', '')
		appointment = request.POST.get('appointment', '')
		latitude = request.POST.get('longitude','')
		longitude = request.POST.get('latitude', '')
		timing = request.POST.get('timing', '')
		#clinic Details 2
		clinic_type2 = request.POST.get('clinic-type2', '')
		clinicName2 = request.POST.get('clinicName2', '')
		address2 = request.POST.get('address2', '')
		city2 = request.POST.get('city2', '')
		number2 = request.POST.get('number2', '')
		fee2 = request.POST.get('fee2', '')
		services2 = request.POST.get('services2', '')
		appointment2 = request.POST.get('appointment2', '')
		latitude2 = request.POST.get('longitude2', '')
		longitude2 = request.POST.get('latitude2', '')
		timing2 = request.POST.get('timing2', '')

		##MAKE EMAIL##
		recepient = 'doctorsinfo.pk@gmail.com'
		subject = "Registration Request | " + practitioner_name
		body = "Practitioner Details\n\n" + "Name: " + practitioner_name + "\n" + "Email: " + email + "\n" + "Credentials: " +credentials + "\n" + "Achievements: " + achievements + "\n" + "Experience: " + experience + "\n" + "Speciality: " + speciality + "\n\n"
		body = body + "Clinic Details:\n\n" + "Clinic Type: " + clinic_type1 + "Clinic Name: " + clinicName + "\n" + "Address: " + address + "\n" + "City: " +city + "\n" + "Number" + number + "\n" + "Fee: " + fee + "\n" + "Services: " + services + "\n" + "Appointment_only: " + appointment + "\n" + "Latitude: " + latitude + "\n" + "Longitude: " + longitude + "\n" + "Timing: " + timing + "\n\n"
		if clinicName2 and address2 and city2 and number2:
			body = body + "Clinic Details 2:\n\n" + "Clinic Type: " + clinic_type2 + "Clinic Name: " + clinicName2 + "\n" + "Address: " + address2 + "\n" + "City: " +city2 + "\n" + "Number" + number2 + "\n" + "Fee: " + fee2 + "\n" + "Services: " + services2 + "\n" + "Appointment_only: " + appointment2 + "\n" + "Latitude: " + latitude2 + "\n" + "Longitude: " + longitude2 + "\n" + "Timing: " + timing2 + "\n\n"
		#send email
		send_mail(subject, body, email, [recepient])
		return render_to_response('practitioner/success.html',{'email': email}, context_instance=RequestContext(request))