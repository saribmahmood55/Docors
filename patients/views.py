from patients.models import *
from practitioner.models import *
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
import json

#
def favourite(user,slug):
	practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	patient = Patient.patient_objects.patient_details(user)
	favourite_list = patient.favt_practitioner.all().filter(slug=slug)
	if not favourite_list.exists():
		patient.favt_practitioner.add(practitioner)#update many to many field
		msg = "Practitioner has been bookmarked, Click on your profile to access directly."
		print msg
		#messages.add_message(request, messages.INFO, msg)

def patient(request):
	data = {}
	if request.user.is_authenticated():
		data['user'] = request.user
	else:
		data['user'] = None
	if request.method == 'GET':
		if data['user']:
			try:
				data['patient'] = Patient.patient_objects.patient_details(data['user'])
				data['reviews'] = PractitionerReview.pr_objects.patient_reviews(data['user'])
				data['specialities'] = Specialization.objects.order_by('name')
			except Patient.DoesNotExist:
				raise Http404
		else:
			data['user'] = None
	if request.method == 'POST':
		if request.user.is_authenticated():
			slug = request.POST.get('slug', None)
			fname = request.POST.get('fname', None)
			lname = request.POST.get('lname', None)
			number = request.POST.get('number', 0)
			#age = request.POST.get('age', None)
			gender = request.POST.get('gender', None)
			if slug:
				user = request.user
				favourite(user, slug)
				return redirect(reverse('practitioner', kwargs={'slug':slug}))
			else:
				p = get_object_or_404(Patient, user=user)
				p.user.first_name=fname
				p.user.last_name=lname
				p.user.save()
				p.cell_number=number
				p.gender=gender
				p.save()
				data['patient'] = Patient.patient_objects.patient_details(user)
				print "Ok"
				data['reviews'] = PractitionerReview.pr_objects.patient_reviews(user)
		else:
			data['patient'] = None
	return render_to_response('patients/profile.html', {'data': data}, context_instance=RequestContext(request))

#
#
def newReview(user, slug, review_text):
	patient = Patient.patient_objects.patient_details(user=user)
	practitioner = Practitioner.prac_objects.practitioner_slug(slug)
	pr, created = PractitionerReview.objects.get_or_create(patient=patient, practitioner=practitioner)
	if not created:
		msg = "You can only review a particular Practitioner once. :/"
		#messages.add_message(request, messages.INFO, msg)
		print msg
	else:
		pr.practitioner = practitioner
		pr.patient = patient
		pr.review_text = review_text
		pr.up_votes = 0
		pr.down_votes = 0
		pr.save()
		print "new review"

##
def Vote(user,review_id, what):
	votes = {}
	patient = Patient.patient_objects.patient_details(user=user)
	review = PractitionerReview.pr_objects.review(review_id)
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


def addReview(request):
	slug = None
	if request.method == "POST":
		if request.user.is_authenticated():
			user = request.user
			slug = request.POST.get('slug', None)
			print slug
			review_text = request.POST.get('review_text', None)
			if slug:
				newReview(user, slug, review_text)
	
	return HttpResponseRedirect(reverse('practitioner', kwargs={'slug': slug}))
	#return HttpResponseRedirect(reverse('practitioner', args=[slug]))


def review(request, review_id):
	slug, votes = None, {}
	if request.method == "POST":
		if request.user.is_authenticated():
			user = request.user
			review = PractitionerReview.pr_objects.review(review_id)
			slug = review.practitioner.slug
			print slug
			up = request.POST.get('up', None)
			down = request.POST.get('down', None)
			if up == "up" and not down:
				what = True
				votes = Vote(user, review_id, what)
			elif down == "down" and not up:
				what = False
				votes = Vote(user, review_id, what)
			if request.is_ajax():
				return HttpResponse(json.dumps(votes), content_type="application/json")
	return HttpResponseRedirect(reverse('practitioner', kwargs={'slug': slug}))