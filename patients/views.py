from patients.models import *
from practitioner.models import *
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import render

#Patient.objects.filter(user=user).update(cell_number='0000001')

def patient(request):
	user = request.user
	if request.method == 'GET':
		if user.is_authenticated:
			if user.username == "AnonymousUser":
				user = None
			else:
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