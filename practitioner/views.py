from practitioner.models import *
from patients.models import Patient
from reviews.models import Review
from practice.models import *
from practitioner.form import PractitionerForm
from utility import *
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
import json


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
		#Get Recent Searches
		try:
			data['recentSearches'] = RecentSearch.objects.order_by('-hit_count')
		except RecentSearch.DoesNotExist:
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
		form = PractitionerForm(request.POST, request.FILES)
		if form.is_valid() and validReCaptcha(request):
			#practitioner
			practitioner_name = form.cleaned_data['practitioner_name']
			email = form.cleaned_data['email']
			credentials = form.cleaned_data['credentials']
			achievements = form.cleaned_data['achievements']
			experience = form.cleaned_data['experience']
			message = form.cleaned_data['message']
			spec = form.cleaned_data['specialities']
			# Create practitioner
			practitioner = Practitioner(name=practitioner_name, email=email, credentials=credentials, achievements=achievements, experience=experience, 
				message=message, status=False)
			practitioner.save()
			speciality = Specialization.objects.get(pk=spec)
			practitioner.specialities.add(speciality)
			
			#PracticeLocation
			practice_name = form.cleaned_data['practice_name']
			address = form.cleaned_data['address']
			city_id = form.cleaned_data['city']
			city = City.objects.get(pk=city_id)
			lon = form.cleaned_data['lon']
			lat = form.cleaned_data['lat']
			#create PracticeLocation
			practice_location = PracticeLocation(name=practice_name, clinic_address=address, city=city, lon=lon, lat=lat)
			practice_location.save()
			#Practice
			practice_type = form.cleaned_data['practice_type']
			practice_photo = form.cleaned_data['practice_photo']
			contact_number = form.cleaned_data['contact_number']
			checkup_fee = form.cleaned_data['checkup_fee']
			services = form.cleaned_data['services']
			appointment = form.cleaned_data['appointment']
			#Create Practice
			practice = Practice(practice_type=practice_type, practice_photo = practice_photo, practice_location=practice_location, practitioner=practitioner, 
				contact_number=contact_number, checkup_fee=checkup_fee, services=services, appointments_only=appointment)
			practice.save()
			#PracticeTiming
			day_from = int(form.cleaned_data['day_from'])
			day_to = int(form.cleaned_data['day_to'])
			start_time = int(form.cleaned_data['start_time'])
			end_time = int(form.cleaned_data['end_time'])
			#Create PracticeTiming
			for day in range(day_from-1, day_to):
				pt = PracticeTiming(practitioner=practitioner, practice=practice, day=day+1, start_time=start_time, end_time=end_time)
				pt.save()
			#send email
			confirmation_mail(practitioner)
			return render_to_response('practitioner/success.html',{'email': email}, context_instance=RequestContext(request))
		else:
			print 're-captcha errors', form.errors
	else:
		form = PractitionerForm()
	return render_to_response('practitioner/registration.html', {'form': form}, context_instance=RequestContext(request))