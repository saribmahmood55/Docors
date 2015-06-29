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
	msg, emailSub, smsSub = None, None, None
	practitioner = Practitioner.objects.get(slug=slug)
	if email != '':
		emailSub = Subscription.subscription_objects.subscription_email_details(email, practitioner)
		if emailSub.exists():
			msg = "You have already been Subscribed for updates about <strong>"+practitioner.name+"</strong> Practice Details through email."
			if cell_number != '':
				smsSub = Subscription.subscription_objects.subscription_mobile_details(cell_number, practitioner)
				if smsSub.exists():
					msg = "You have already been Subscribed for updates about <strong>"+practitioner.name+"</strong> Practice Details through email and sms."
				else:
					emailSub.update(cell_number=cell_number)
					msg = "You have been subscribed for sms and email updates about <strong>"+practitioner.name+"</strong> Practice Details."
		elif cell_number != '':
			smsSub = Subscription.subscription_objects.subscription_mobile_details(cell_number, practitioner)
			if smsSub.exists():
				smsSub.update(email=email)
			else:
				sub = Subscription(email=email,cell_number=cell_number,practitioner=practitioner)
				sub.save()
			msg = "You have been subscribed for sms and email updates about <strong>"+practitioner.name+"</strong> Practice Details."
		else:
			sub = Subscription(email=email,cell_number=None,practitioner=practitioner)
			sub.save()
			msg = "You have been subscribed for updates about <strong>"+practitioner.name+"</strong> Practice Details through email."
	elif cell_number != '':
		smsSub = Subscription.subscription_objects.subscription_mobile_details(cell_number, practitioner)
		if smsSub.exists():
			msg = "You have already been Subscribed for updates about <strong>"+practitioner.name+"</strong> Practice Details through sms."
		else:
			sub = Subscription(email=None,cell_number=cell_number,practitioner=practitioner)
			sub.save()
			msg = "You have been subscribed for updates about <strong>"+practitioner.name+"</strong> Practice Details through sms."	
	return msg