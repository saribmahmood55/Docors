from patients.models import *
from practitioner.models import *
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse

def patient(request):
	patient, reviews, specialities, user = None, None, None, None
	if request.user.is_authenticated():
		user = request.user
	else:
		user = None
	if request.method == 'GET':
		if user:
			try:
				patient = Patient.patient_objects.patient_details(user)
				reviews = PractitionerReview.pr_objects.patient_reviews(user)
				specialities = Specialization.objects.order_by('name')
			except Patient.DoesNotExist:
				raise Http404
		else:
			patient = None
	if request.method == 'POST':
		if request.user.is_authenticated():
			fname = request.POST.get('fname', None)
			lname = request.POST.get('lname', None)
			number = request.POST.get('number', 0)
			#age = request.POST.get('age', None)
			gender = request.POST.get('gender', None)
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
	return render(request, 'patients/profile.html', {'patient': patient, 'reviews': reviews, 'specialities' : specialities})


def upVote(user, review_id):
	review = ReviewStats.prs_objects.review(review_id,user)
	if review.exists():
		if review[0].status == 1:
			msg = "Review Up-Voted, already."
			print msg
			#messages.add_message(request, messages.INFO, msg)
		else:
			review_ = ReviewStats.objects.get(review__pk=review_id)
			review_.status = 1
			review_.save()
			msg = "Review Up-Voted."
			print msg
			#messages.add_message(request, messages.INFO, msg)
	else:
		patient = Patient.patient_objects.patient_details(user)
		review = PractitionerReview.pr_objects.review(review_id)
		reviewStat = ReviewStats()
		reviewStat.review = review
		reviewStat.patient = patient
		reviewStat.status = 1
		reviewStat.save()
		review.down_votes += 1
		review.save()
		msg = "Review Up-Voted."
		print msg
		#messages.add_message(request, messages.INFO, msg)


def downVote(user, review_id):
	review = ReviewStats.prs_objects.review(review_id,user)
	if review.exists():
		if review[0].status == -1:
			msg = "Review Down-Voted, already."
			print msg
			#messages.add_message(request, messages.INFO, msg)
		else:
			review_ = ReviewStats.objects.get(review__pk=review_id)
			review_.status = -1
			review_.save()
			msg = "Review Down-Voted."
			print msg
			#messages.add_message(request, messages.INFO, msg)
	else:
		patient = Patient.patient_objects.patient_details(user)
		review = PractitionerReview.pr_objects.review(review_id)
		reviewStat = ReviewStats()
		reviewStat.review = review
		reviewStat.patient = patient
		print review.review_text
		reviewStat.status = 1
		reviewStat.save()
		review.down_votes += 1
		review.save()
		msg = "Review Down-Voted."
		print msg
		#messages.add_message(request, messages.INFO, msg)


def review(request, review_id):
	if request.method == "POST":
		if request.user.is_authenticated():
			user = request.user
			review = PractitionerReview.pr_objects.review(review_id)
			slug = review.practitioner.slug
			up = request.POST.get('up', None)
			down = request.POST.get('down', None)
			if up == "up":
				upVote(user, review_id)
				print "up"
			elif down == "down":
				downVote(user, review_id)
				print "down"
	return redirect(reverse('practitioner', kwargs={'slug':slug}))
#
#	