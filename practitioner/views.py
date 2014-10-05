from practitioner.models import Practitioner, Specialization, ClinicLocation, ClinicLocationTiming
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


#home page
def index(request):
	try:
		specialities = Specialization.objects.order_by('name')
	except Specialization.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/index.html', {'specialities': specialities}, context_instance=RequestContext(request) )


#handle search request
def search(request):
	name, speciality, experience, day, practitioner_list, clinic_list = None, None, None, None, [], []
	if request.method == "POST":
		name = request.POST.get('prac_name', None)
		speciality = request.POST.get('speciality', None)
		experience = request.POST.get('experience', None)
		day = request.POST.get('day', None)
		if speciality == "Select Speciality":
			speciality = None
		if day == "Select Day":
			day = None
		if experience == 0:
			experience = None
	try:
		if name != None and speciality == None:
			practitioner_list = Practitioner.prac_objects.practitioner_name(name)
			print 1
		elif speciality != None and name == None:
			practitioner_list = Practitioner.prac_objects.practitioner_speciality(speciality)
			print 2
		elif name != None and speciality != None and day == None:
			practitioner_list = Practitioner.prac_objects.practitioner_name_and_speciality(name, speciality)
			print 3
		elif experience != None and speciality != None and name == None:
			practitioner_list = Practitioner.prac_objects.practitioner_experienced(experience,speciality)
			print 4
		elif day != None and speciality != None:
			clinic_list = Clinic_List(speciality, day)
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioners.html',
		{'practitioners': practitioner_list, 'clinics': clinic_list}, 
		context_instance=RequestContext(request))


# single practitioner details
def practitioner(request, slug):
	try:
		practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioner.html', {'practitioner': practitioner}, context_instance=RequestContext(request))


'''
def Clinic_List(speciality, day):
	clinic_list = ClinicLocation.cl_objects.clinic_speciality(speciality,day)
	return clinic_list
'''

def Clinic_Detail(request):
	try:
		clinic_detail = ClinicLocation.cl_objects.clinic_detail(clinic_name)
	except ClinicLocation.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/clinic_detail.html', {'one_clinic': clinic_detail}, context_instance=RequestContext(request))

'''
from practitioner.views import *
practitioner_detail = Practitioner.prac_objects.practitioner_detail('Dr. Mohammad Anwar')
print practitioner_detail[0].name

from practitioner.views import *
cl = Clinic_List('Pediatric (Child)','Monday')
print len(cl)

clinic_detail = ClinicLocation.cl_objects.clinic_detail('Dr. Mohammad Anwar Private Clininc')
print clinic_detail
def Clinic_List(day, speciality):
	print "called"
	try:
		clinic_list = ClinicLocation.cl_objects.clinic_speciality(day,speciality)
	except ClinicLocation.DoesNotExist:
		raise Http404
	print len(clinic_list)
	return render_to_response('practitioner/clinic_list.html', {'clinics': clinic_list})
'''