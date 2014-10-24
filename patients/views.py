from patients.models import Patient
from reviews.models import *
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
				data['reviews'] = Review.review_objects.patient_reviews(data['user'])
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