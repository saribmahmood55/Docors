# flake8: noqa
from django.forms.models import modelform_factory
from practitioner.models import *
from practice.models import *
from patients.models import Patient
from reviews.models import Question, Review
from practitioner.forms import *
from utility import *
from django.forms.formsets import formset_factory
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from haystack.query import SearchQuerySet
import json

from docors.utility import get_city, get_ip

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
            elif type_query == "practice":
                sqs = SearchQuerySet().filter(name=query).models(PracticeLocation)
                for x in sqs:
                    res.append({'value':x.object.name, 'type':type_query, 'href':x.object.slug})
            else:
                sqs = SearchQuerySet().filter(name=query).models(Practitioner)
                for x in sqs:
                    res.append({'value':x.object.full_name, 'type':type_query, 'href':x.object.slug})

            res = [dict(t) for t in set([tuple(d.items()) for d in res])]
            return HttpResponse(json.dumps(res),content_type="application/json")
        else:
            data = {}
            try:
                city = get_city(request)
                data['practice'] = Practice.practice_objects.practitioner_name(name=query,city=city)
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

#individual item click in the autocomplete list
def get_search_practice(request):
    if request.method == "GET":
        type = request.GET.get("search.type","")
        query = request.GET.get("q","")
        return HttpResponseRedirect(reverse('practice_search', kwargs={'slug': query, 'typee': type}))

#reverse match view for the "#individual item click in the autocomplete list"
def practitionerSearch(request, slug, typee):
    data = dict()
    practice = []
    data['results_header'] = "Practitioner"
    city = get_city(request)

    if typee == "specialization":
        sqs = Specialization.objects.get(slug=slug)
        data['results_header'] = "Practitioner(s) who Specialize in " + sqs.name
        data['practice'] = Practice.practice_objects.get_practice_by_specialty(specialty=sqs,city=city)
    elif typee == "condition":
        sqs = Condition.objects.get(slug=slug)
        data['results_header'] = "Practitioner(s) who treat " + sqs.name + " condition"
        data['practice'] = Practice.practice_objects.get_practice_by_condition(condition=sqs,city=city)
    elif typee == "procedure":
        sqs = Procedure.objects.get(slug=slug)
        data['results_header'] = "Practitioner(s) who perform " + sqs.name + " procedure"
        data['practice'] = Practice.practice_objects.get_practice_by_procedure(procedure=sqs,city=city)

    data['ob'] = sqs

    data['results_count'] = len(data['practice'])
    return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

#reverse match view for the "#individual item click in the autocomplete list"
def practice_search(request, slug, typee):
    data = dict()

    city = get_city(request)

    data['practice'] = Practice.practice_objects.get_practice_by_location(slug=slug,city=city)

    data['ob'] = PracticeLocation.objects.get(slug=slug)

    data['results_header'] = "Practitioner(s) in " + data['ob'].name

    data['results_count'] = len(data['practice'])
    return render_to_response('practitioner/results.html', {'data': data}, context_instance=RequestContext(request))

def claim_practitioner(request, slug):
    if request.method == "POST":
        form = ClaimPractitionerForm(request.POST)
        if form.is_valid():
            new_claim = form.save(slug)
            return render_to_response("practitioner/claim_pending.html", {'claim': new_claim}, context_instance=RequestContext(request))
        else:
            print form.errors
    else:
        form = ClaimPractitionerForm()
    practitioner = Practitioner.objects.get(slug=slug)
    return render_to_response('practitioner/claim.html', {'practitioner':practitioner,'form': form}, context_instance=RequestContext(request))

def update_info_practitioner(request, slug):
    if request.method == "POST":
        form = UpdateInfoForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                new_info = form.save(request.user.email,slug)
            else:
                new_info = form.save(get_ip(request), slug)
            return render_to_response("practitioner/updateinfo_pending.html", {'info': new_info}, context_instance=RequestContext(request))
        else:
            print form.errors
    else:
        form = UpdateInfoForm()
    practitioner = Practitioner.objects.get(slug=slug)
    return render_to_response('practitioner/updateinfo.html', {'practitioner':practitioner,'form': form}, context_instance=RequestContext(request))

def profile(request, slug):
    data = dict()
    if request.method == "GET":
        data['practitioner'] = Practitioner.objects.get(slug=slug)
        data['practice'] = Practice.practice_objects.practice_detail(slug)
        form = EditProfileForm(instance=data['practitioner'])
        return render_to_response('practitioner/edit.html', {'data':data,'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def new_review(request,slug):
    data = dict()
    try:
        patient = request.user.patient
        data['practitioner'] = Practitioner.objects.get(slug=slug)
    except Patient.DoesNotExist:
        raise Http404

    if Review.review_objects.review_exists(patient,data['practitioner']):
        return HttpResponseRedirect(reverse('practitioner', kwargs={'slug': slug}))
    else:
        questions = Question.objects.all()[0]
        if request.method == "POST":
            answerForm = AnswerForm(request.POST)
            commentForm = CommentForm(request.POST)
            if answerForm.is_valid():
                answers = answerForm.save()
                if commentForm.is_valid():
                    comments = commentForm.save()
                    review = Review(patient=patient, practitioner=data['practitioner'], answers=answers, comments=comments)
                    review.save()
                    return render_to_response('practitioner/review_success.html', {'new_review':review}, context_instance=RequestContext(request))
                else:
                    review = Review(patient=patient, practitioner=data['practitioner'], answers=answers)
                    review.save()
                    return render_to_response('practitioner/review_success.html', {'new_review':review}, context_instance=RequestContext(request))
        elif request.method == "GET":
            answerForm = AnswerForm()
            commentForm = CommentForm()
        return render_to_response('practitioner/review.html', {'data':data,'answerForm':answerForm, 'commentForm':commentForm, 'questions':questions}, context_instance=RequestContext(request))

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
    PractitionerForm = modelform_factory(Practitioner, fields = ['full_name','photo','gender','year_of_birth','email','physician_type','degrees','specialty','fellowship','completion_year','conditions','procedures','experience','message','achievements'])
    PracticeFormSet = formset_factory(PracticeForm,formset=BasePracticeFormSet, extra=2, max_num=2, can_delete=True)
    if request.method == 'POST':
        pract_form = PractitionerForm(request.POST, request.FILES)
        practice_formset = PracticeFormSet(request.POST, request.FILES)
        if pract_form.is_valid() and practice_formset.is_valid():
            practitioner = pract_form.save()
            extraPracticeTimings = list()
            for i in range(2):
                extraPracticeTimings.append({'day':request.POST.getlist("extra_day_"+str(i)),'start_time':request.POST.getlist("extra_start_time_"+str(i)),'end_time':request.POST.getlist("extra_end_time_"+str(i))})
            print extraPracticeTimings
            practice_formset.save(practitioner,extraPracticeTimings)
            return render_to_response('practitioner/success.html',{'email': 'test@email.com'}, context_instance=RequestContext(request))
        else:
            print practice_formset.errors
            pract_form = PractitionerForm()
            practice_formset = PracticeFormSet()
            error_occured = True
    else:
        pract_form = PractitionerForm()
        practice_formset = PracticeFormSet()
    return render_to_response('practitioner/registration.html', {'error_occured':error_occured, 'pract_form': pract_form,'practice_formset': practice_formset}, context_instance=RequestContext(request))

#to populate the condition procedure field in the doctor registration page
def get_condition_procedure(request):
    if request.is_ajax():
        data = {}
        value = request.GET.get('value','')
        if value == "":
            value = Specialization.spec_objects.get_default_id()
        data['fellowship'] = ["<option value='"+str(f.id)+"'>"+str(f)+"</option>" for f in Fellowship.objects.filter(specialization=Specialization.objects.get(pk=value))]
        data['conditions'] = ["<option value='"+str(c.id)+"'>"+str(c)+"</option>" for c in Condition.objects.filter(specialization=Specialization.objects.get(pk=value))]
        data['procedures'] = ["<option value='"+str(p.id)+"'>"+str(p)+"</option>" for p in Procedure.objects.filter(specialization=Specialization.objects.get(pk=value))]
        return HttpResponse(json.dumps(data),content_type="application/json")

def get_practice_names(request):
    if request.is_ajax():
        practice_q = request.GET.get('q','')
        practice_type = request.GET.get('type','')
        practice_names = Practice.practice_objects.practice_names(name=practice_q,p_type=practice_type)
        suggestions = [{'id':result.id,'text':result.practice_location.name} for result in practice_names]
        the_data = json.dumps(suggestions)
        return HttpResponse(the_data, content_type='application/json')

def get_practice_details(request):
    if request.is_ajax():
        practice_id = request.GET.get('practice_id','')
        practice_location = Practice.objects.get(id=practice_id).practice_location
        print practice_id
        print practice_location
        data = json.dumps({'address':practice_location.clinic_address,'city':practice_location.area.city.id,'area_id':practice_location.area.id,'area_name':practice_location.area.name, 'contact_number':practice_location.contact_number})
        return HttpResponse(data, content_type='application/json')
