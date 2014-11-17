from reviews.views import *
from patients.models import Patient
from practice.models import Practice
from practitioner.models import Practitioner
from reviews.models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def newReview(user, prac_slug, practice_slug, review_text):
	practice, review = None, {}
	patient = Patient.patient_objects.patient_details(user=user)
	practitioner = Practitioner.prac_objects.practitioner_slug(prac_slug)
	if practice_slug:
		practice = Practice.objects.get(practice_location__slug=practice_slug)
	pr = Review.objects.filter(patient=patient, practitioner=practitioner, practice=practice)
	if pr.exists():
		review["msg"] = "Sorry. You can post Review about a particular Practitioner only once. :/"
		#messages.add_message(request, messages.INFO, msg)
	else:
		pr = Review()
		pr.practitioner = practitioner
		pr.patient = patient
		pr.practice = practice
		pr.review_text = review_text
		pr.save()
		review["patient"] = user.username
		review["review_text"] = review_text
	return review

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