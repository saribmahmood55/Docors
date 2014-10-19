from patients.models import *
from practitioner.models import *
from django.http import Http404
from django.shortcuts import render

#Patient.objects.filter(user=user).update(cell_number='0000001')

def patient(request):
	user = request.user
	if user.is_authenticated:
		try:
			patient = Patient.patient_objects.patient_details(user)
			reviews = PractitionerReview.pr_objects.patient_reviews(user) 
		except Patient.DoesNotExist:
			raise Http404
	return render(request, 'patients/profile.html', {'patient': patient, 'reviews': reviews})


def updatePatient(request):
	user = request.user
	if request.method == "POST":
		field = request.POST.get('id')
        value = request.POST.get('value')
	if user.is_authenticated:
		try:
			Patient.objects.filter(user=user).update(cell_number=value)
			patient = Patient.patient_objects.patient_details(user)
			reviews = PractitionerReview.pr_objects.patient_reviews(user)
		except Patient.DoesNotExist:
			raise Http404
	else:
		patient = None
	return render(request, 'patients/profile.html', {'patient': patient, 'reviews': reviews})

def favourite(request):
	user, slug, error = None, None, None
	user = request.user
	if request.method == "POST":
		slug = request.POST.get('slug', None)
	
	if user.is_authenticated:	
		practitioner = Practitioner.prac_objects.practitioner_slug(slug)
		patient = Patient.patient_objects.patient_details(user)
		favourite = patient.favt_practitioner.all().filter(slug=slug)
		if not favourite:
			patient.favt_practitioner.add(practitioner)
		else:
			error = "Already favourited"
	else:
		error = "Not a registered user."
	return render(request, 'patients/profile.html', {'patient': patient, 'error': error})


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
	patient = Patient.patient_objects.patient_details(user=user)
	p = PractitionerReview()
	p.practitioner = practitioner
	p.patient = patient
	p.review_text = reviewText
	p.up_votes = 0
	p.down_votes = 0
	p.save()
	try:
		practise = Practise.practise_objects.practise_detail(slug)
		practise_timing = PractiseTiming.pt_objects.practise_timing_details(slug)
		reviews = PractitionerReview.pr_objects.practitioner_reviews(slug)
	except Practitioner.DoesNotExist:
		raise Http404
	return render(request, 'practitioner/practitioner.html', 
		{'practitioner': practitioner, 'practise': practise, 'practise_timing': practise_timing, 'reviews': reviews, 'patient': user})