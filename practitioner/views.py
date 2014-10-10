from practitioner.models import *
from patients.models import *
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


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
		if speciality == "Select Speciality":
			speciality = None
		if day == "Select Day":
			day = None
		if experience == 0:
			experience = None
	try:
		#name
		if name != None and speciality == None:
			practitioner_list = Practitioner.prac_objects.practitioner_name(name)
		#specialty
		elif speciality != None and name == None and experience == None:
			practitioner_list = Practitioner.prac_objects.practitioner_speciality(speciality)
		#name and specialty
		elif name != None and speciality != None and day == None:
			practitioner_list = Practitioner.prac_objects.practitioner_name_and_speciality(name, speciality)
		#specialty and experience
		elif experience != None and speciality != None:
			print 4
			practitioner_list = Practitioner.prac_objects.practitioner_experienced(experience,speciality)
		#specialty and day
		elif day != None and speciality != None:
			clinic_list = ClinicLocation.cl_objects.clinic_speciality(speciality,day)
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioners.html',
		{'practitioners': practitioner_list, 'clinics': clinic_list, 'search_specialty': speciality, 'search_city': city},
		context_instance=RequestContext(request))


# single practitioner details
def practitioner(request, slug):
	try:
		practitioner = Practitioner.prac_objects.practitioner_slug(slug)
		clinic = ClinicLocation.cl_objects.clinic_detail_slug(slug)
		clinic_timing = ClinicLocationTiming.ct_objects.clinic_details(slug)
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