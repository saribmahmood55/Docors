from practitioner.models import *
from patients.models import *
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.core.mail import send_mail

#home page
def index(request):
	user = request.user
	if user.username == "AnonymousUser":
		request.user = None
	try:
		specialities = Specialization.objects.order_by('name')
		cities = City.objects.order_by('name')
	except Specialization.DoesNotExist:
		raise Http404
	return render(request, 'practitioner/index.html', 
		{'specialities': specialities, 'cities': cities, 'patient': user},context_instance=RequestContext(request))


#handle search request
def q(request):
	user, city, name, speciality, experience, day, practise = None, None, None, None, None, None, []
	user = request.user
	if user.username == "AnonymousUser":
		request.user = None
	if request.method == "GET":
		city = request.GET.get('city', None)
		name = request.GET.get('name', None)
		speciality = request.GET.get('spec', None)
		experience = request.GET.get('exp', None)
		day = request.GET.get('day', None)
		if speciality == "Select Speciality":
			speciality = None
		if day == "Select Day":
			day = None

	try:
		#testing
		practise = Practise.practise_objects.practise_details(city, name, speciality, experience, day)
		#print len(prac_clinic_list)
	except Practise.DoesNotExist:
		raise Http404
	return render(request, 'practitioner/results.html', {'practise': practise, 'patient': user})


# single practitioner details
def practitioner(request, slug):
	favt = None
	user = request.user
	if user.is_authenticated:
		patient = Patient.patient_objects.patient_details(user)
		favourite = patient.favt_practitioner.all().filter(slug=slug)
		if favourite:
			favt = True
	try:
		practitioner = Practitioner.prac_objects.practitioner_slug(slug)
		practise = Practise.practise_objects.practise_detail(slug)
		practise_timing = PractiseTiming.pt_objects.practise_timing_details(slug)
		reviews = PractitionerReview.pr_objects.practitioner_reviews(slug)
	except Practitioner.DoesNotExist:
		raise Http404
	return render(request, 'practitioner/practitioner.html', 
		{'practitioner': practitioner, 'practise': practise, 'practise_timing': practise_timing, 'reviews': reviews, 'patient': user, 'favt': favt})


#send email
def register(request):
	email, practitioner_name = None, None
	if request.method == "POST":
		practitioner_name = request.POST.get('practitioner_name', None)
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