from practitioner.models import *
from practitioner.serializers import PractitionerSerializer, SpecializationSerializer, DegreeSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from patients.models import Patient
from reviews.models import Review
from practice.models import *
from practitioner.form import PractitionerForm
from practitioner.tasks import confirmation_mail
from utility import *
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin
import json

class FacebookLogin(SocialLogin):
	adapter_class = FacebookOAuth2Adapter

def index(request):
	data = {}
	data['specialities'] = Specialization.objects.order_by('slug')
	data['completeness'] = 0

	try:
		patient_data = Patient.patient_objects.patient_details(lambda: request.user if request.user.is_authenticated() else None)
		data['completeness'] = eval("+".join(["10" if patient_data.age_group else "0","10" if patient_data.gender else "0","10" if patient_data.cell_number else "0","20" if data['user'].first_name else "0","20" if data['user'].last_name else "0","10" if data['user'].username else "0","20" if data['user'].email else "0"]))

	except Patient.DoesNotExist:
		pass
	
	return render_to_response('index.html', {'data': data}, context_instance=RequestContext(request))

def practitioner_suggestions(request):
	if request.method == "GET":
		query = request.GET.get('q', '')
		if request.is_ajax():
			results = Practitioner.prac_objects.practitioner_suggest(query)
			return HttpResponse(json.dumps(list(results)),content_type="application/json")
		else:
			data = {}

			try:
				data['practice'] = Practice.practice_objects.practitioner_name(query)
				data['results_count'] = len(data['practice']['practice_list'])
				data['results_header'] = "physicians matching your search criteria"
			except Practice.DoesNotExist:
				raise Http404
			
			return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))


#advance search
def adv(request):
	data = {}
	if request.method == "GET":
		try:
			data['specialities'] = Specialization.objects.order_by('human_name')
			data['cities'] = City.objects.order_by('pk')
		except Specialization.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/advance.html', {'data': data}, context_instance=RequestContext(request))	

def login(request):
	if request.method == "POST":
		request.session.set_test_cookie()
	else:
		login_form = AuthenticationForm()
	return render_to_response('practitioner/advance.html', {'login_form': login_form}, context_instance=RequestContext(request))	


def registration(request):
	if request.method == 'POST':
		form = PractitionerForm(request.POST, request.FILES)
		if form.is_valid():
			
			#practitioner
			p_title = form.cleaned_data['practitioner_title']
			practitioner_name = form.cleaned_data['practitioner_name']
			email = form.cleaned_data['email']
			p_type = form.cleaned_data['physician_type']
			p_gender = form.cleaned_data['practitioner_gender']
			birth_year = form.cleaned_data['year_of_birth']
			achievements = form.cleaned_data['achievements']
			experience = form.cleaned_data['experience']
			message = form.cleaned_data['message']
			spec = form.cleaned_data['specialities']
			
			# Create practitioner
			practitioner = Practitioner(title=p_title, name=practitioner_name, gender=p_gender, year_of_birth=birth_year, email=email, physician_type=p_type, achievements=achievements, experience=experience, message=message, status=False)
			practitioner.save()

			#Add Degress to practitioner
			credentials = form.cleaned_data['credentials']
			cred_dict = credentials.split(",")
			for cred in cred_dict:
				degree = Degree.degree_objects.get_degree(cred)
				practitioner.degrees.add(degree)

			#Add Speciality to practitioner
			speciality = Specialization.objects.get(pk=spec)
			#print speciality
			practitioner.specialities.add(speciality)

			#PracticeLocation
			practice_name = form.cleaned_data['practice_name']
			address = form.cleaned_data['address']
			photo = ''#form.cleaned_data['practice_photo']
			city_id = form.cleaned_data['city']
			city = City.objects.get(pk=city_id)
			lon = ''#form.cleaned_data['lon']
			lat = ''#form.cleaned_data['lat']
			contact_number = form.cleaned_data['contact_number']
			
			#create PracticeLocation
			practice_location = PracticeLocation(name=practice_name, contact_number=contact_number, clinic_address=address, city=city)
			practice_location.save()
			
			#Practice
			practice_type = form.cleaned_data['practice_type']
			checkup_fee_id = form.cleaned_data['checkup_fee']
			checkup_fee = CheckupFee.objects.get(pk=checkup_fee_id)
			services = ''#form.cleaned_data['services']
			appointment = form.cleaned_data['appointment']
			
			#Create Practice
			practice = Practice(practice_type=practice_type, practice_location=practice_location, practitioner=practitioner, fee=checkup_fee, services=services, appointments_only=appointment)
			practice.save()
			#PracticeTiming
			day_from = int(form.cleaned_data['day_from'])
			day_to = int(form.cleaned_data['day_to'])
			start_time = form.cleaned_data['start_time']
			end_time = form.cleaned_data['end_time']
			#Create PracticeTiming
			for day in range(day_from-1, day_to):
				pt = PracticeTiming(practitioner=practitioner, practice=practice, day=day+1, start_time=start_time, end_time=end_time)
				pt.save()
			#send email
			#email_details = {'name': practitioner_name, 'email': email, 'slug': practitioner.slug}
			#confirmation_mail.delay(email_details)
			return render_to_response('practitioner/success.html',{'email': email}, context_instance=RequestContext(request))
		else:
			print 're-captcha errors', form.errors
	else:
		form = PractitionerForm()
	degrees = Degree.objects.all()
	degree_name = [deg.name for deg in degrees]
	return render_to_response('practitioner/registration.html', {'form': form,'degree_list':degree_name}, context_instance=RequestContext(request))