from practitioner.models import *
from patients.models import *
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail

#home page
def index(request):
	try:
		specialities = Specialization.objects.order_by('name')
		cities = City.objects.order_by('name')
	except Specialization.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/index.html', 
		{'specialities': specialities, 'cities': cities},context_instance=RequestContext(request))


#handle search request
def search(request):
	city, name, speciality, experience, day, practitioner_list, clinic_list = None, None, None, None, None, [], []
	if request.method == "POST":
		city = request.POST.get('city', None)
		name = request.POST.get('prac_name', None)
		speciality = request.POST.get('speciality', None)
		experience = request.POST.get('experience', None)
		day = request.POST.get('day', None)
		
		if city == "Select City":
			city = None
		if name == "":
			name = None
		if speciality == "Select Speciality":
			speciality = None
		if day == "Select Day":
			day = None
		if experience == 0:
			experience = None
	try:
		#name
		if name != None and speciality == None and experience == None and day == None:
			practitioner_list = Practitioner.prac_objects.practitioner_name(name)
		#speciality
		elif speciality != None and name == None and experience == None:
			practitioner_list = Practitioner.prac_objects.practitioner_speciality(speciality)
		#name and speciality
		elif name != None and speciality != None and day == None:
			practitioner_list = Practitioner.prac_objects.practitioner_name_and_speciality(name, speciality)
		#speciality and experience
		elif experience != None and speciality != None and day == None and name == None:
			print experience
			practitioner_list = Practitioner.prac_objects.practitioner_experienced(experience,speciality)
		#day and speciality
		elif day != None and speciality != None and name == None and experience == None:
			practitioner_list = ClinicLocationTiming.ct_objects.practitioner_day_specialty(speciality,day)
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioners.html',
		{'practitioners': practitioner_list, 'search_specialty': speciality, 'search_city': city, 'day': day},
		context_instance=RequestContext(request))


# single practitioner details
def practitioner(request, slug):
	try:
		practitioner = Practitioner.prac_objects.practitioner_slug(slug)
		clinic = ClinicLocation.cl_objects.clinic_details(slug)
		clinic_timing = ClinicLocationTiming.ct_objects.clinic_timing_details(slug)
		reviews = PractitionerReview.pr_objects.practitioner_reviews(slug)
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioner.html', 
		{'practitioner': practitioner, 'clinic': clinic, 'clinic_timing': clinic_timing, 'reviews': reviews},
		context_instance=RequestContext(request))


def Clinic_Detail(request):
	try:
		clinic_detail = ClinicLocation.cl_objects.clinic_detail(clinic_name)
	except ClinicLocation.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/clinic_detail.html', {'one_clinic': clinic_detail},context_instance=RequestContext(request))


#send email
def register(request):
	email, practitioner_name = None, None
	if request.method == "POST":
		global practitioner_name
		practitioner_name = request.POST.get('practitioner_name', None)
		global email
		email = request.POST.get('email', None)
		credentials = request.POST.get('credentials', None)
		achievements = request.POST.get('achievements', None)
		experience = request.POST.get('experience', None)
		speciality = request.POST.get('speciality', None)
		#Clinic Details 1
		clinicName = request.POST.get('clinicName', None)
		address = request.POST.get('address', None)
		city = request.POST.get('city', None)
		number = request.POST.get('number', None)
		fee = request.POST.get('fee', None)
		services = request.POST.get('services', None)
		appointment = request.POST.get('appointment', None)
		latitude = request.POST.get('longitude', None)
		longitude = request.POST.get('latitude', None)
		timing = request.POST.get('timing', None)
		#clinic Details 2
		clinicName2 = request.POST.get('clinicName2', None)
		address2 = request.POST.get('address2', None)
		city2 = request.POST.get('city2', None)
		number2 = request.POST.get('number2', None)
		fee2 = request.POST.get('fee2', None)
		services2 = request.POST.get('services2', None)
		appointment2 = request.POST.get('appointment2', None)
		latitude2 = request.POST.get('longitude2', None)
		longitude2 = request.POST.get('latitude2', None)
		timing2 = request.POST.get('timing2', None)

	##MAKE EMAIL##
	recepient = 'docors2014@gmail.com'
	subject = "Registration Request | " + practitioner_name
	body = "Practitioner Details\n\n" + "Name: " + practitioner_name + "\n" + "Email: " + email + "\n" + "Credentials: " +credentials + "\n" + "Achievements: " + achievements + "\n" + "Experience: " + experience + "\n" + "Speciality: " +speciality + "\n\n"
	body = body + "Clinic Details\n\n" + "Clinic Name: " + clinicName + "\n" + "Address: " + address + "\n" + "City: " +city + "\n" + "Number" + number + "\n" + "Fee: " + fee + "\n" + "Services: " + services + "\n" + "Appointment_only: " + appointment + "\n" + "Latitude: " + latitude + "\n" + "Longitude: " + longitude + "\n" + "Timing: " + timing + "\n\n"
	if clinicName2 and address2 and city2 and number2:
		body = body + "Clinic Details 2\n\n" + "Clinic Name: " + clinicName2 + "\n" + "Address: " + address2 + "\n" + "City: " +city2 + "\n" + "Number" + number2 + "\n" + "Fee: " + fee2 + "\n" + "Services: " + services2 + "\n" + "Appointment_only: " + appointment2 + "\n" + "Latitude: " + latitude2 + "\n" + "Longitude: " + longitude2 + "\n" + "Timing: " + timing2 + "\n\n"
	#send email
	send_mail(subject, body, email, [recepient])
	return render_to_response('practitioner/success.html',{'email': email}, context_instance=RequestContext(request))

'''
from practitioner.views import *
practitioner_detail = Practitioner.prac_objects.practitioner_detail('Dr. Mohammad Anwar')
print practitioner_detail[0].name

from practitioner.views import *
cl = Clinic_List('Pediatric (Child)','Monday')
print len(cl)

clinic_detail = ClinicLocation.cl_objects.clinic_detail('Dr. Mohammad Anwar Private Clininc')
print clinic_detail
'''