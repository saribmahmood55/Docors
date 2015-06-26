from reviews.views import *
from patients.models import Patient
from practice.models import Practice
from practitioner.models import Practitioner
from reviews.models import *
from badwordsfilter import *
#from django.contrib import messages

def newReview(user, slug, review_text):
	clean_text = badWordFilter(review_text)
	print clean_text
	patient = Patient.patient_objects.patient_details(user=user)
	practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	pr = Review.objects.filter(patient=patient, practitioner=practitioner)
	if pr.exists():
		return "Sorry. You can post Review about a particular Practitioner only once. !!"
		#messages.set_level(request, messages.ERROR)
		#messages.error(request, "Sorry. You can post Review about a particular Practitioner only once. !!")
	else:
		pr = Review()
		pr.practitioner = practitioner
		pr.patient = patient
		pr.review_text = clean_text
		pr.save()
		return 1

#
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
			else:
				rs.status = 1
				rs.save()
				review.up_votes += 1
				review.down_votes -= 1
				votes['up']=review.up_votes
				votes['down']=review.down_votes
				review.save()
		else:
			if rs.status == -1:
				rs.save()
				votes['up']=review.up_votes
				votes['down']=review.down_votes
			else:
				rs.status = -1
				rs.save()
				review.up_votes -= 1
				review.down_votes += 1
				votes['up']=review.up_votes
				votes['down']=review.down_votes
				review.save()
	else:
		if what:
			rs.status = 1
			rs.save()
			review.up_votes += 1
			votes['up']=review.up_votes
			votes['down']=review.down_votes
			review.save()
		else:
			rs.status = -1
			rs.save()
			review.down_votes += 1
			votes['up']=review.up_votes
			votes['down']=review.down_votes
			review.save()
	return votes