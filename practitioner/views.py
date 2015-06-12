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
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin
import json

class FacebookLogin(SocialLogin):
	adapter_class = FacebookOAuth2Adapter


class PractitionerList(generics.ListCreateAPIView):
	queryset = Practitioner.objects.all()
	serializer_class = PractitionerSerializer


class PractitionerTileList(APIView):
	def get(self, request, format=None):
		practitioner_title = [
			{"1" : "Dr. "}, 
			{"2" : "Prof. "}, 
			{"3" : "Prof. Dr. "}
		]
		return Response(practitioner_title)


class PractitionerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Practitioner.objects.all()
	serializer_class = PractitionerSerializer

class SpecializationList(generics.ListCreateAPIView):
	queryset = Specialization.objects.all()
	serializer_class = SpecializationSerializer

class SpecializationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Specialization.objects.all()
	serializer_class = SpecializationSerializer

class DegreeList(generics.ListCreateAPIView):
	queryset = Degree.objects.all()
	serializer_class = DegreeSerializer

class DegreeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Degree.objects.all()
	serializer_class = DegreeSerializer

class PhysicianTypeList(APIView):
	def get(self, request, format=None):
		physician_types = [
			{"id":1,"value":"1","title":"Trainee"}, 
			{"id":2,"value":"2","title":"Specialist"}
		]
		return Response(physician_types)

class PhysicianTitleList(APIView):
	def get(self, request, format=None):
		title_types = [
			{"id":1,"value":"1","title":"Dr. "}, 
			{"id":2,"value":"2","title":"Prof. "},
			{"id":3,"value":"3","title":"Prof. Dr. "}
		]
		return Response(title_types)

class PhysicianGenderList(APIView):
	def get(self, request, format=None):
		gender_types = [
			{"id":1,"value":"M","title":"Male"}, 
			{"id":2,"value":"F","title":"Female"},
		]
		return Response(gender_types)

def index(request):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None

	data['completeness'] = 0

	try:
		patient_data = Patient.patient_objects.patient_details(data['user'])
		if patient_data.age_group:
			data['completeness'] = data['completeness'] + 10
		if patient_data.gender:
			data['completeness'] = data['completeness'] + 10
		if patient_data.cell_number:
			data['completeness'] = data['completeness'] + 10
		if data['user'].first_name:
			data['completeness'] = data['completeness'] + 20
		if data['user'].last_name:
			data['completeness'] = data['completeness'] + 20
		if data['user'].username:
			data['completeness'] = data['completeness'] + 10
		if data['user'].email:
			data['completeness'] = data['completeness'] + 20

	except Patient.DoesNotExist:
		pass
	
	return render_to_response('index.html', {'data': data}, context_instance=RequestContext(request))

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