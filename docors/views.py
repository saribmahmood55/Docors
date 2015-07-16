from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from practitioner.models import *
from patients.models import Patient
from hitcount.models import HitCount
from django.contrib.contenttypes.models import ContentType

from .utility import *
from docors.forms import *

# Create your views here.

#main page
def index(request):
	data = {'popular_pract':list(),'popular_proc':list()}
	data['specialities'] = Specialization.objects.order_by('slug')
	data['completeness'] = 0
	contents_types = dict()
	for hc in HitCount.objects.filter(content_type=ContentType.objects.get_for_model(Practitioner)).order_by('-hits')[:5]:
		data['popular_pract'].append(hc.content_object)
	for hc in HitCount.objects.filter(content_type=ContentType.objects.get_for_model(Procedure)).order_by('-hits')[:5]:
		data['popular_proc'].append(hc.content_object)

	try:
		patient_data = Patient.patient_objects.patient_details(lambda: request.user if request.user.is_authenticated() else None)
		#data['completeness'] = eval("+".join(["10" if patient_data.age_group else "0","10" if patient_data.gender else "0","10" if patient_data.cell_number else "0","20" if data['user'].first_name else "0","20" if data['user'].last_name else "0","10" if data['user'].username else "0","20" if data['user'].email else "0"]))

	except Patient.DoesNotExist:
		pass

	print get_lat_lon(request)

	data['doc_form'],data['spec_form'],data['adv_form'] = doctors_form(),speciality_form(),advanced_form()
	
	return render_to_response('index.html', {'data': data}, context_instance=RequestContext(request))

#advance search
def adv(request):
	data = {}
	if request.method == "GET":
		try:
			data['specialities'] = Specialization.objects.order_by('human_name')
			data['cities'] = City.objects.order_by('pk')
		except Specialization.DoesNotExist:
			raise Http404
	return render_to_response('practitioner/advance.html', {'data': data}, context_instance=RequestContext(request))	