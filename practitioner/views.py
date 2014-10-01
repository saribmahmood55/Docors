from django.http import Http404
from docors.settings import *
from django.shortcuts import render_to_response
from practitioner.models import Practitioner, Specialization, ClinicLocation, ClinicLocationTiming

def docors(request):
	try:
		specialities = Specialization.objects.order_by('name')
	except ClinicLocation.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/index.html', {'specialities': specialities})


def Practitioner_List(request, name=None, speciality=None, experience=None):
	try:
		if name and not speciality:
			prac_list = Practitioner.prac_objects.practitioner_name(name)
		elif speciality and not name:
			prac_list = Practitioner.prac_objects.practitioner_speciality(speciality)
		elif name and speciality:
			prac_list = Practitioner.prac_objects.practitioner_name_and_specialty(name, speciality)
		elif experience and speciality and not name:
			prac_list = Practitioner.prac_objects.practitioner_experienced(experience,speciality)
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioner_list.html', {'practitioners': prac_list})


def Practitioner_Details(request, prac_name):
	try:
		practitioner = Practitioner.prac_objects.practitioner_name(prac_name)
	except Practitioner.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/practitioner_detail.html', {'one_practitioner': practitioner})


def Clinic_List(day,speciality):
	try:
		clinic_list = ClinicLocation.cl_objects.clinic_speciality(day,speciality)
	except ClinicLocation.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/clinic_list.html', {'clinics': clinic_list})


def Clinic_Detail(request, clinic_name):
	try:
		clinic_detail = ClinicLocation.cl_objects.clinic_detail(clinic_name)
	except ClinicLocation.DoesNotExist:
		raise Http404
	return render_to_response('practitioner/clinic_detail.html', {'clinics': clinic_detail})