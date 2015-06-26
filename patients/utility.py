from patients.models import *
from practitioner.models import Practitioner, Specialization
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
		msg = "Practitioner already Favourite"
		return False
		#messages.add_message(request, messages.INFO, msg)
def  deleteFavtPrac(patient, slug):
	practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	patient.favt_practitioner.remove(practitioner)
	return True

#
def interestedSpecAdd(user,slug):
	specialization = Specialization.spec_objects.spec_slug(slug)
	patient = Patient.patient_objects.patient_details(user)
	int_spec_list = patient.interested_specialities.all().filter(slug=slug)
	if not int_spec_list.exists():
		patient.interested_specialities.add(specialization)#update many to many field
		return True
	else:
		return False

#
def interestedSpecRemove(user,slug):
	specialization = Specialization.spec_objects.spec_slug(slug)
	patient = Patient.patient_objects.patient_details(user)
	patient.interested_specialities.remove(specialization)
	return True

#
def deleteReview(review_id):
	review = Review.review_objects.review(review_id)
	review.delete()
	return True
#
def updateReview(review_id, review_text):
	review = Review.review_objects.review(review_id)
	review.update(review_text=review_text, review_date=auto_now)
	return True

#
def excludedSpecialities(patient):
	favt_spec = []
	for spec in patient.interested_specialities.all():
		favt_spec.append(spec.slug)
	return Specialization.objects.exclude(slug__in=favt_spec)

#
def getAllSpecialities():
	return Specialization.objects.all()

#
def newSubscription(slug, email, cell_number):
	msg, patient, emailSub, smsSub = None, None, None, None
	practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	if email != '':
		patient = Patient.patient_objects.registered_patient(email)
		if patient.exists():
			patient = Patient.patient_objects.patient_details(patient)
			favourite_list = patient.favt_practitioner.all().filter(slug=slug)
			if not favourite_list.exists():
				patient.favt_practitioner.add(practitioner)
				msg = "Practitioner has been bookmarked, Click on your profile to access directly."
			else:
				msg = "You have already been Subscribed for updates about "+practitioner.name+" Practice Details through email."
			return msg
		emailSub = Subscription.subscription_objects.subscription_email_details(email, practitioner)
		if emailSub.exists():
			msg = "You have already been Subscribed for updates about "+practitioner.name+" Practice Details through email."
			if cell_number != '':
				smsSub = Subscription.subscription_objects.subscription_mobile_details(cell_number, practitioner)
				if smsSub.exists():
					msg = "You have already been Subscribed for sms updates about "+practitioner.name+" Practice Details."
				else:
					emailSub.update(cell_number='12345678')
					msg = "You have been subscribed for sms updates about "+practitioner.name+" Practice Details."
		else:
			sub = Subscription()
			sub.email = email
			sub.practitioner = practitioner
			sub.cell_number = ''
			sub.save()
			msg = "You have been subscribed for updates about "+practitioner.name+" Practice Details through email."
	elif cell_number != '' and email == '':
		smsSub = Subscription.subscription_objects.subscription_mobile_details(cell_number, practitioner)
		if smsSub.exists():
			msg = "You have already been Subscribed for sms about "+practitioner.name+" Practice Details."
		else:
			sub = Subscription()
			sub.cell_number = cell_number
			sub.email = ''
			sub.practitioner = practitioner
			sub.save()
			msg = "You have been subscribed for sms updates about "+practitioner.name+" Practice Details."	
	return msg