from django.shortcuts import render
from patients.models import Patient
from practitioner.models import Practitioner
from utility import *
from reviews.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import json


def addReview(request):
	prac_slug = None
	if request.method == "POST":
		if request.user.is_authenticated():
			user = request.user
			prac_slug = request.POST.get('slug', None)
			practice_slug = request.POST.get('practice_slug', None)
			review_text = request.POST.get('review_text', None)
			if prac_slug:
				newReview(user, prac_slug, practice_slug, review_text)
		return HttpResponseRedirect(reverse('practitioner', kwargs={'slug': prac_slug}))


def review(request, review_id):
	slug, votes = None, {}
	if request.method == "POST":
		if request.user.is_authenticated():
			user = request.user
			review = Review.review_objects.review(review_id)
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
#