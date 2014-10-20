from patients.models import *
from practitioner.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render

#Patient.objects.filter(user=user).update(cell_number='0000001')

def patient(request):
	user = request.user
	if request.method == 'GET':
		if user.is_authenticated:
			try:
				patient = Patient.patient_objects.patient_details(user)
				reviews = PractitionerReview.pr_objects.patient_reviews(user) 
			except Patient.DoesNotExist:
				raise Http404
		else:
			patient = None
	if request.method == 'POST':
		fname = request.POST.get('fname', None)
		lname = request.POST.get('lname', None)
		number = request.POST.get('number', 0)
		#age = request.POST.get('age', None)
		gender = request.POST.get('gender', None)
		print "Name: %s , %s Num: %s Gender: %s" % (fname,lname,number,gender)
		if user.is_authenticated:
			p = get_object_or_404(Patient, user=user)
			p.user.first_name=fname
			p.user.last_name=lname
			p.user.save()
			p.cell_number=number
			p.gender=gender
			p.save()
			patient = Patient.patient_objects.patient_details(user)
			print "Ok"
			reviews = PractitionerReview.pr_objects.patient_reviews(user)
		else:
			patient = None
	return render(request, 'patients/profile.html', {'patient': patient, 'reviews': reviews})


def updatePatient(request):
	user = request.user
	print user.username
	#fname, lname, number, age, gender = None, None, 0, None, None
	
	#return render(request, 'patients/profile.html', {'patient': patient, 'reviews': reviews})

'''
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
'''

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