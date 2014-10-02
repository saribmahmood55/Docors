from django.http import Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from practitioner.models import Practitioner, Specialization, ClinicLocation, ClinicLocationTiming

def index(request):
	try:
		specialities = Specialization.objects.order_by('name')
	except ClinicLocation.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/index.html', {'specialities': specialities})


@csrf_exempt
def practitioners(request):
	name, speciality, experience, day, practitioner_list = None, None, None, None, [] 
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
			try:
				clinic_list = Clinic_List(speciality, day)
				print len(clinic_list)
			except ClinicLocation.DoesNotExist:
				raise Http404	
			return render_to_response('practitioner/clinic_list.html', {'clinics': clinic_list})
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioner_list.html', {'practitioners': practitioner_list})


@csrf_exempt
def practitioner_detail(request, practitioner_id):
	try:
		practitioner_detail = Practitioner.objects.get(pk=practitioner_id)
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioner_detail.html', {'one_practitioner': practitioner_detail})


def Clinic_List(speciality, day):
	clinic_list = ClinicLocation.cl_objects.clinic_speciality(speciality,day)
	return clinic_list


@csrf_exempt
def Clinic_Detail(request):
	try:
		clinic_detail = ClinicLocation.cl_objects.clinic_detail(clinic_name)
	except ClinicLocation.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/clinic_detail.html', {'one_clinic': clinic_detail})

'''
from practitioner.views import *
cl = Clinic_List('Pediatric (Child)','Monday')
print len(cl)


clinic_detail = ClinicLocation.cl_objects.clinic_detail('Dr. Mohammad Anwar Private Clininc')
print clinic_detail



@csrf_exempt
def Clinic_List(day, speciality):
	print "called"
	try:
		clinic_list = ClinicLocation.cl_objects.clinic_speciality(day,speciality)
	except ClinicLocation.DoesNotExist:
		raise Http404
	print len(clinic_list)
	return render_to_response('practitioner/clinic_list.html', {'clinics': clinic_list})
'''