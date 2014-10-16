from patients.models import *
from practitioner.models import *
from django.http import Http404
from django.shortcuts import render


def patient(request):
	user = request.user
	try:
		patient = Patient.objects.get(user=user)
	except Patient.DoesNotExist:
		raise Http404
	return render(request, 'patients/profile.html', {'patient': patient})


def favourite(request):
	user, slug = None, None
	if request.method == "POST":
		user = request.user
		slug = request.POST.get('slug', None)
		practitioner = Practitioner.prac_objects.practitioner_slug(slug)
		print practitioner.name
		#patient = Patient.patient_objects.patient_details(user)
		Patient.objects.filter(user=user).update(cell_number='0000001')
	try:
		patient = Patient.objects.get(user=user)
	except Patient.DoesNotExist:
		raise Http404
	return render(request, 'patients/profile.html', {'patient': patient})
	
'''
	try:
		clinic = ClinicLocation.cl_objects.clinic_detail(slug)
		clinic_timing = ClinicLocationTiming.ct_objects.clinic_timing_details(slug)
		reviews = PractitionerReview.pr_objects.practitioner_reviews(slug)
	except Practitioner.DoesNotExist:
		raise Http404
	return render(request, 'practitioner/practitioner.html', 
		{'practitioner': practitioner, 'clinic': clinic, 'clinic_timing': clinic_timing, 'reviews': reviews, 'patient': user})
'''


def up(request):
	return 0

def down(request):
	return 0

def addReview(request):
	user, reviewText, slug = None, None, None
	user = request.user
	if request.method == "POST":
		reviewText = request.POST.get('review_text', None)
		slug = request.POST.get('slug', None)
	practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	patient = Patient.objects.get(user=user)
	p = PractitionerReview()
	p.practitioner = practitioner
	p.patient = patient
	p.review_text = reviewText
	p.up_votes = 0
	p.down_votes = 0
	p.save()
	try:
		clinic = ClinicLocation.cl_objects.clinic_detail(slug)
		clinic_timing = ClinicLocationTiming.ct_objects.clinic_timing_details(slug)
		reviews = PractitionerReview.pr_objects.practitioner_reviews(slug)
	except Practitioner.DoesNotExist:
		raise Http404
	return render(request, 'practitioner/practitioner.html', 
		{'practitioner': practitioner, 'clinic': clinic, 'clinic_timing': clinic_timing, 'reviews': reviews, 'patient': user})