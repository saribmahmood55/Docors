# flake8: noqa
from practitioner.models import *
from patients.models import Patient
from reviews.models import Review
from practice.models import *
from practitioner.form import PractitionerForm
from practitioner.tasks import confirmation_mail
from utility import *
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.safestring import mark_safe
from haystack.query import SearchQuerySet
from hitcount.models import HitCount
from django.contrib.contenttypes.models import ContentType
import json

#to populate the typeahead input field
def practitioner_suggestions(request):
	if request.method == "GET":
		query = request.GET.get('q', '')
		type_query = request.GET.get('type', 'practitioner')
		if request.is_ajax():
			res = []
			#results = Practitioner.prac_objects.practitioner_suggest(query)
			if type_query == "specialization":
				sqs = SearchQuerySet().filter(name=query).models(Specialization)
				for x in sqs:
					res.append({'value':x.object.human_name, 'type':type_query, 'href':x.object.slug})
			elif type_query == "condition":
				sqs = SearchQuerySet().filter(name=query).models(Condition)
				for x in sqs:
					res.append({'value':x.object.name, 'type':type_query, 'href':x.object.slug})
			elif type_query == "procedure":
				sqs = SearchQuerySet().filter(name=query).models(Procedure)
				for x in sqs:
					res.append({'value':x.object.name, 'type':type_query, 'href':x.object.slug})
			else:
				sqs = SearchQuerySet().filter(name=query).models(Practitioner)
				for x in sqs:
					res.append({'value':x.object.name, 'type':type_query, 'href':x.object.slug})

			res = [dict(t) for t in set([tuple(d.items()) for d in res])]
			return HttpResponse(json.dumps(res),content_type="application/json")
		else:
			data = {}
			try:
				data['practice'] = Practice.practice_objects.practitioner_name(query)
				data['results_count'] = len(data['practice'])
				data['results_header'] = "physicians matching your search criteria"
			except Practice.DoesNotExist:
				raise Http404
			
			return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

#individual item click in the autocomplete list
def get_search_practitioner(request):
	if request.method == "GET":
		type = request.GET.get("search.type","")
		query = request.GET.get("q","")
		return HttpResponseRedirect(reverse('practitionerSearch', kwargs={'slug': query, 'typee': type}))

#reverse match view for the "#individual item click in the autocomplete list"
def practitionerSearch(request, slug, typee):
	data = dict()
	practice = []
	data['results_header'] = "Practitioner"

	if typee == "specialization":
		sqs = Specialization.objects.get(slug=slug)
		data['results_header'] = "Practitioner(s) who Specialize in " + slug
	elif typee == "condition":
		sqs = Condition.objects.get(slug=slug)
		data['results_header'] = "Practitioner(s) who treat " + slug + " condition"
	elif typee == "procedure":
		sqs = Procedure.objects.get(slug=slug)
		data['results_header'] = "Practitioner(s) who perform " + slug + " procedure"

	data['ob'] = sqs

	for prac in sqs.practitioner_set.all():
		for x in Practice.practice_objects.practitioner_name(prac.name):
			practice.append(x)
	data['practice'] = practice
	data['results_count'] = len(practice)
	return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

#custom login function to redirect if already logged in
def login(request):
	if request.method == "POST":
		request.session.set_test_cookie()
	else:
		login_form = AuthenticationForm()
	return render_to_response('practitioner/advance.html', {'login_form': login_form}, context_instance=RequestContext(request))	

#doctors registration view
def registration(request):
	error_occured = False
	if request.method == 'POST':
		form = PractitionerForm(request.POST, request.FILES)
		if form.is_valid():
			
			#practitioner
			practitioner_name = form.cleaned_data['practitioner_name']
			email = form.cleaned_data['email']
			p_type = form.cleaned_data['physician_type']
			p_gender = form.cleaned_data['practitioner_gender']
			birth_year = form.cleaned_data['year_of_birth']
			achievements = form.cleaned_data['achievements']
			experience = form.cleaned_data['experience']
			message = form.cleaned_data['message']
			spec = form.cleaned_data['specialities']
			
			# Create practitioner
			practitioner = Practitioner(name=practitioner_name, gender=p_gender, year_of_birth=birth_year, email=email, physician_type=p_type, achievements=achievements, experience=experience, message=message, status=False)
			practitioner.save()

			#Add Degress to practitioner
			credentials = form.cleaned_data['credentials']
			cred_dict = credentials.split(",")
			for cred in cred_dict:
				degree = Degree.degree_objects.get_degree(cred)
				practitioner.degrees.add(degree)

			#Add Conditions to practitioner
			conditions = form.cleaned_data['conditions']
			cond_dict = conditions.split(",")
			print cond_dict
			for cond in cond_dict:
				condition = Condition.condition_objects.get_condition(cond)
				practitioner.conditions.add(condition)

			#Add Procedures to practitioner
			procedures = form.cleaned_data['procedures']
			proc_dict = procedures.split(",")
			print proc_dict
			for proc in proc_dict:
				procedure = Procedure.procedure_objects.get_procedure(proc)
				practitioner.procedures.add(procedure)

			#Add Speciality to practitioner, updated from M2M field to Foreign key relation by Asad
			speciality = Specialization.objects.get(pk=spec)
			practitioner.speciality = speciality

			#PracticeLocation
			practice_name = form.cleaned_data['practice_name']
			address = form.cleaned_data['address']
			photo = ''#form.cleaned_data['practice_photo']
			area_id = form.cleaned_data['area']
			area = Area.objects.get(pk=area_id)
			lon = form.cleaned_data['lon']
			lat = form.cleaned_data['lat']
			contact_number = form.cleaned_data['contact_number']
			
			#create PracticeLocation
			practice_location = PracticeLocation(name=practice_name, contact_number=contact_number, clinic_address=address, area=area, lon=lon, lat=lat)
			practice_location.save()
			
			#Practice
			practice_type = form.cleaned_data['practice_type']
			checkup_fee_id = form.cleaned_data['checkup_fee']
			checkup_fee = CheckupFee.objects.get(pk=checkup_fee_id)
			appointment = form.cleaned_data['appointment']
			
			#Create Practice
			practice = Practice(practice_type=practice_type, practice_location=practice_location, practitioner=practitioner, fee=checkup_fee, appointments_only=appointment)
			practice.save()

			#PracticeTiming
			day_from = int(form.cleaned_data['day_from'])
			day_to = int(form.cleaned_data['day_to'])
			start_time = form.cleaned_data['start_time']
			end_time = form.cleaned_data['end_time']
			#Create PracticeTiming
			for day in range(day_from-1, day_to):
				pt = PracticeTiming(practice=practice, day=day+1, start_time=start_time, end_time=end_time)
				pt.save()
			#send email
			email_details = {'name': practitioner_name, 'email': email, 'slug': practitioner.slug}
			confirmation_mail.delay(email_details)
			return render_to_response('practitioner/success.html',{'email': email}, context_instance=RequestContext(request))
		else:
			form = PractitionerForm()
			error_occured = True
	else:
		form = PractitionerForm()
	degrees = Degree.objects.all()
	degree_name = [deg.name for deg in degrees]
	return render_to_response('practitioner/registration.html', {'error_occured':error_occured, 'form': form, 'degree_list':degree_name}, context_instance=RequestContext(request))

#to populate the condition procedure field in the doctor registration page
def get_condition_procedure(request):
	if request.is_ajax():
		data = {}
		value = request.GET.get('value','')
		data['conditions'] = ["<option value='"+str(c.id)+"'>"+str(c)+"</option>" for c in Condition.objects.filter(specialization=Specialization.objects.get(pk=value))]
		data['procedures'] = ["<option value='"+str(p.id)+"'>"+str(p)+"</option>" for p in Procedure.objects.filter(specialization=Specialization.objects.get(pk=value))]
		return HttpResponse(json.dumps(data),content_type="application/json")