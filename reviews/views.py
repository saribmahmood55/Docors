from django.shortcuts import render
from patients.models import Patient
from practitioner.models import Practitioner
from utility import *
from reviews.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
import json


def addReview(request):
	review, slug = {}, None
	if request.method == "POST":
		if request.user.is_authenticated():
			user = request.user
			slug = request.POST.get('slug', None)
			review_text = request.POST.get('review_text', None)
			review['msg'] = newReview(user, slug, review_text)
			if request.is_ajax():
				return HttpResponse(json.dumps(review), content_type="application/json")
	return HttpResponseRedirect(reverse('practitioner', kwargs={'slug': slug}))


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