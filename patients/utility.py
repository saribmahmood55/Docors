from patients.models import *
from practitioner.models import Specialization
from practitioner.models import Practitioner
from django.shortcuts import get_object_or_404
from reviews.models import Review

#
def updatePatientDetails(patientDetails):
	p = get_object_or_404(Patient, user=patientDetails['user'])
	p.user.first_name = patientDetails['fname']
	p.user.last_name = patientDetails['lname']
	p.user.save()
	p.cell_number = patientDetails['number']
	p.gender = patientDetails['gender']
	p.age_group = patientDetails['age']
	p.save()
#

def favourite(user,slug):
	practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	patient = Patient.patient_objects.patient_details(user)
	favourite_list = patient.favt_practitioner.all().filter(slug=slug)
	if not favourite_list.exists():
		patient.favt_practitioner.add(practitioner)#update many to many field
		msg = "Practitioner has been bookmarked, Click on your profile to access directly."
		print msg
		return True
	else:
		return False
		#messages.add_message(request, messages.INFO, msg)
def  deleteFavtPrac(patient, slug):
	practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	print practitioner
	patient.favt_practitioner.remove(practitioner)
	return True

#
def deleteReview(review_id):
	review = Review.review_objects.review(review_id)
	review.delete()
	return True
#
def excludedSpecialities(patient):
	favt_spec = []
	for spec in patient.interested_specialities.all():
		favt_spec.append(spec.slug)
	return Specialization.objects.exclude(slug__in=favt_spec)