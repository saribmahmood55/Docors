from reviews.views import *
from patients.models import Patient
from practice.models import Practice
from practitioner.models import Practitioner
from reviews.models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def newReview(user, prac_slug, practice_slug, review_text):
	practice = None
	patient = Patient.patient_objects.patient_details(user=user)
	practitioner = Practitioner.prac_objects.practitioner_slug(prac_slug)
	if practice_slug:
		practice = Practice.objects.get(practice_location__slug=practice_slug)
		print practice
	pr = Review.objects.filter(patient=patient, practitioner=practitioner, practice=practice)
	if pr.exists():
		msg = "You can only review a particular Practitioner once. :/"
		#messages.add_message(request, messages.INFO, msg)
		print msg
	else:
		pr = Review()
		pr.practitioner = practitioner
		pr.patient = patient
		pr.practice = practice
		pr.review_text = review_text
		pr.up_votes = 0
		pr.down_votes = 0
		pr.save()
		print "new review"

##
##
def Vote(user,review_id, what):
	votes = {}
	patient = Patient.patient_objects.patient_details(user=user)
	review = Review.review_objects.review(review_id)
	rs, created = ReviewStats.objects.get_or_create(patient=patient, review=review)
	if not created:
		if what:
			if rs.status == 1:
				rs.save()
				votes['up']=review.up_votes
				votes['down']=review.down_votes
				msg = "Review up-Voted, already."
				print msg
			else:
				rs.status = 1
				rs.save()
				review.up_votes += 1
				review.down_votes -= 1
				votes['up']=review.up_votes
				votes['down']=review.down_votes
				review.save()
				msg = "Review up-Voted."
				print msg
		else:
			if rs.status == -1:
				rs.save()
				votes['up']=review.up_votes
				votes['down']=review.down_votes
				msg = "Review down-Voted, already."
				print msg
			else:
				rs.status = -1
				rs.save()
				review.up_votes -= 1
				review.down_votes += 1
				votes['up']=review.up_votes
				votes['down']=review.down_votes
				review.save()
				print "Review down-Voted."
	else:
		if what:
			rs.status = 1
			rs.save()
			review.up_votes += 1
			votes['up']=review.up_votes
			votes['down']=review.down_votes
			review.save()
			print "new Review up-Voted."
		else:
			rs.status = -1
			rs.save()
			review.down_votes += 1
			votes['up']=review.up_votes
			votes['down']=review.down_votes
			review.save()
			print "new Review down-Voted."
	return votes