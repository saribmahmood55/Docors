from django.forms.formsets import formset_factory
from django.forms.models import modelform_factory
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from haystack.query import SearchQuerySet
import json

from practitioner.models import Practitioner
from practitioner.models import Specialization
from practitioner.models import Condition
from practitioner.models import Procedure
from practitioner.models import Fellowship

from practice.models import Practice
from practice.models import PracticeLocation

from patients.models import Patient

from reviews.models import Question
from reviews.models import Review

from practitioner.forms import BasePracticeFormSet
from practitioner.forms import PracticeForm
from practitioner.forms import ClaimPractitionerForm
from practitioner.forms import UpdateInfoForm
from practitioner.forms import EditProfileForm
from practitioner.forms import AnswerForm
from practitioner.forms import CommentForm

from docors.utility import get_city, get_ip


# to populate the typeahead input field
def suggestions_practitioner(request):
    if request.method == "GET":
        query = request.GET.get('q', '')
        if request.is_ajax():
            results = {
                'Specialization': {'text': 'Specialization', 'children': []},
                'Fellowship': {'text': 'Fellowship', 'children': []},
                'Condition': {'text': 'Conditions Treated', 'children': []},
                'Procedure': {'text': 'Procedures Performed', 'children': []},
                'PracticeLocation': {'text': 'Hospital/Clinic', 'children': []},
                'Practitioner': {'text': 'Practitioner', 'children': []}
            }
            sqs = SearchQuerySet().autocomplete(name=query)
            for x in sqs:
                if x.object.__class__.__name__ == "Practitioner":
                    results[x.object.__class__.__name__]['children'].append(
                        {'id': x.object.pk,
                         'text': x.object.full_name,
                         'type': x.object.__class__.__name__,
                         'slug': x.object.slug
                         }
                    )
                else:
                    results[x.object.__class__.__name__]['children'].append(
                        {'id': x.object.pk,
                         'text': x.object.name,
                         'type': x.object.__class__.__name__,
                         'slug': x.object.slug
                         }
                    )
            res = [
                value
                for key, value in results.iteritems()
                if value['children']
            ]
            return HttpResponse(
                json.dumps(res),
                content_type="application/json"
            )
        else:
            data = {}
            try:
                city = get_city(request)
                data['practice'] = Practice.practice_objects.practitioner_name(
                    name=query, city=city
                )
                data['results_count'] = len(data['practice'])
                data['results_header'] = "physicians matching \
                    your search criteria"
            except Practice.DoesNotExist:
                raise Http404

            return render_to_response(
                'practitioner/results.html',
                {'data': data},
                context_instance=RequestContext(request)
            )


# individual item click in the autocomplete list
def search_practitioner(request):
    if request.method == "GET":
        searchType = request.GET.get("search.type", "")
        query = request.GET.get("q", "")
        loc = request.GET.get("loc", "lahore")
        print searchType
        print query
        print loc
        if searchType == "Specialization" or searchType == "Fellowship":
            return HttpResponseRedirect(
                reverse(
                    'specialty_fellowship_results',
                    kwargs={
                        'specialty_fellowship': query,
                        'location': loc
                    }
                )
            )
        elif searchType == "Condition":
            print "coming to check"
            return HttpResponseRedirect(
                reverse(
                    'condition_results',
                    kwargs={
                        'condition': query,
                        'location': loc
                    }
                )
            )
        elif searchType == "Procedure":
            return HttpResponseRedirect(
                reverse(
                    'procedure_results',
                    kwargs={
                        'procedure': query,
                        'location': loc
                    }
                )
            )
        elif searchType == "PracticeLocation":
            return HttpResponseRedirect(
                reverse(
                    'practice_results',
                    kwargs={
                        'practice': query,
                        'location': loc
                    }
                )
            )
        else:
            raise Http404


# reverse match view for the "#individual item click in the autocomplete list"
def results_specialty_fellowship(request, specialty_fellowship, location):
    data = dict()
    data['results_header'] = "Practitioner"
    try:
        sqs = Specialization.objects.get(slug=specialty_fellowship)
        data['practice'] = Practice.practice_objects.get_practice_by_specialty(
            specialty=sqs,
            city=location
        )
        data['results_header'] = "Practitioner(s) who Specialize in " + sqs.name
        data['type'] = "specialty"
    except Specialization.DoesNotExist:
        sqs = Fellowship.objects.get(slug=specialty_fellowship)
        data['practice'] = Practice.practice_objects.get_practice_by_fellowship(
            fellowship=sqs,
            city=location
        )
        data['results_header'] = "Practitioner(s) with Fellowship " + sqs.name
        data['type'] = "fellowship"

    data['ob'] = sqs
    data['results_count'] = len(data['practice'])
    return render_to_response(
        'practitioner/results.html',
        {'data': data},
        context_instance=RequestContext(request)
    )


# reverse match view for the "#individual item click in the autocomplete list"
def results_condition(request, condition, location):
    print "coming to condition"
    data = dict()
    data['results_header'] = "Practitioner"
    sqs = Condition.objects.get(slug=condition)
    data['results_header'] = "Practitioner(s) who treat \
        " + sqs.name + " condition"
    data['practice'] = Practice.practice_objects.get_practice_by_condition(
        condition=sqs, city=location
    )
    data['type'] = "condition"

    data['ob'] = sqs
    data['results_count'] = len(data['practice'])
    return render_to_response(
        'practitioner/results.html',
        {'data': data},
        context_instance=RequestContext(request)
    )


# reverse match view for the "#individual item click in the autocomplete list"
def results_procedure(request, procedure, location):
    data = dict()
    data['results_header'] = "Practitioner"
    sqs = Procedure.objects.get(slug=procedure)
    data['results_header'] = "Practitioner(s) who perform \
        " + sqs.name + " procedure"
    data['practice'] = Practice.practice_objects.get_practice_by_procedure(
        procedure=sqs, city=location
    )
    data['type'] = "procedure"

    data['ob'] = sqs
    data['results_count'] = len(data['practice'])
    return render_to_response(
        'practitioner/results.html',
        {'data': data},
        context_instance=RequestContext(request)
    )


# reverse match view for the "#individual item click in the autocomplete list"
def results_practice(request, practice, location):
    data = dict()
    data['results_header'] = "Practitioner"
    sqs = PracticeLocation.objects.get(slug=practice)
    data['practice'] = Practice.practice_objects.get_practice_by_location(
        slug=practice, city=location
    )
    data['results_header'] = "Practitioner(s) in " + sqs.name
    data['searchType'] = "practice"

    data['ob'] = sqs
    data['results_count'] = len(data['practice'])
    return render_to_response(
        'practitioner/results.html',
        {'data': data},
        context_instance=RequestContext(request)
    )


def claim_practitioner(request, slug):
    if request.method == "POST":
        form = ClaimPractitionerForm(request.POST)
        if form.is_valid():
            new_claim = form.save(slug)
            return render_to_response(
                "practitioner/claim_pending.html",
                {'claim': new_claim},
                context_instance=RequestContext(request)
            )
    else:
        form = ClaimPractitionerForm()
    practitioner = Practitioner.objects.get(slug=slug)
    return render_to_response(
        'practitioner/claim.html',
        {'practitioner': practitioner, 'form': form},
        context_instance=RequestContext(request)
    )


def update_info_practitioner(request, slug):
    if request.method == "POST":
        form = UpdateInfoForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                new_info = form.save(request.user.email, slug)
            else:
                new_info = form.save(get_ip(request), slug)
            return render_to_response(
                "practitioner/updateinfo_pending.html",
                {'info': new_info},
                context_instance=RequestContext(request)
            )
    else:
        form = UpdateInfoForm()
    practitioner = Practitioner.objects.get(slug=slug)
    return render_to_response(
        'practitioner/updateinfo.html',
        {'practitioner': practitioner, 'form': form},
        context_instance=RequestContext(request)
    )


def profile_practitioner(request, slug):
    data = dict()
    if request.method == "GET":
        data['practitioner'] = Practitioner.objects.get(slug=slug)
        data['practice'] = Practice.practice_objects.practice_detail(slug)
        form = EditProfileForm(instance=data['practitioner'])
        return render_to_response(
            'practitioner/edit.html',
            {'data': data, 'form': form},
            context_instance=RequestContext(request)
        )


@login_required(login_url='/accounts/login/')
def review_practitioner(request, slug):
    data = dict()
    try:
        patient = request.user.patient
        data['practitioner'] = Practitioner.objects.get(slug=slug)
    except Patient.DoesNotExist:
        raise Http404

    if Review.review_objects.review_exists(patient, data['practitioner']):
        return HttpResponseRedirect(
            reverse(
                'practitioner', kwargs={'slug': slug}
            )
        )
    else:
        questions = Question.objects.all()[0]
        if request.method == "POST":
            answerForm = AnswerForm(request.POST)
            commentForm = CommentForm(request.POST)
            if answerForm.is_valid():
                answers = answerForm.save()
                if commentForm.is_valid():
                    comments = commentForm.save()
                    review = Review(
                        patient=patient,
                        practitioner=data['practitioner'],
                        answers=answers,
                        comments=comments
                    )
                    review.save()
                    return render_to_response(
                        'practitioner/review_success.html',
                        {'new_review': review},
                        context_instance=RequestContext(request)
                    )
                else:
                    review = Review(
                        patient=patient,
                        practitioner=data['practitioner'],
                        answers=answers
                    )
                    review.save()
                    return render_to_response(
                        'practitioner/review_success.html',
                        {'new_review': review},
                        context_instance=RequestContext(request)
                    )
        elif request.method == "GET":
            answerForm = AnswerForm()
            commentForm = CommentForm()
        return render_to_response(
            'practitioner/review.html',
            {
                'data': data,
                'answerForm': answerForm,
                'commentForm': commentForm,
                'questions': questions
            },
            context_instance=RequestContext(request)
        )


# doctors registration view
def registration_practitioner(request):
    PractitionerForm = modelform_factory(
        Practitioner,
        fields=[
            'full_name',
            'photo',
            'gender',
            'email',
            'physician_type',
            'degrees',
            'specialty',
            'fellowship',
            'completion_year',
            'conditions',
            'procedures'
        ]
    )
    PracticeFormSet = formset_factory(
        PracticeForm,
        formset=BasePracticeFormSet,
        extra=2,
        max_num=2,
        can_delete=True
    )
    if request.method == 'POST':
        pract_form = PractitionerForm(request.POST, request.FILES)
        practice_formset = PracticeFormSet(request.POST, request.FILES)
        if pract_form.is_valid() and practice_formset.is_valid():
            practitioner = pract_form.save(commit=False)
            practitioner.set_password('12341234')
            practitioner.save()
            pract_form.save_m2m()
            extraPracticeTimings = list()
            for i in range(2):
                extraPracticeTimings.append(
                    {
                        'day': request.POST.getlist(
                            "extra_day_"+str(i)
                        ),
                        'start_time': request.POST.getlist(
                            "extra_start_time_"+str(i)
                        ),
                        'end_time': request.POST.getlist(
                            "extra_end_time_"+str(i)
                        )
                    }
                )
            practice_formset.save(practitioner, extraPracticeTimings)
            return render_to_response(
                'practitioner/success.html',
                {'email': 'test@email.com'},
                context_instance=RequestContext(request)
            )
    else:
        pract_form = PractitionerForm()
        practice_formset = PracticeFormSet()
    return render_to_response(
        'practitioner/registration.html',
        {'pract_form': pract_form, 'practice_formset': practice_formset},
        context_instance=RequestContext(request)
    )


# to populate the condition procedure field in the doctor registration page
def get_cond_proc_ajax(request):
    if request.is_ajax():
        data = {}
        value = request.GET.get('value', '')
        if value == "":
            value = Specialization.spec_objects.get_default_id()
        data['fellowship'] = ["<option value='"+str(f.id)+"'>"+str(f)+"</option>" for f in Fellowship.objects.filter(specialization=Specialization.objects.get(pk=value))]
        data['conditions'] = ["<option value='"+str(c.id)+"'>"+str(c)+"</option>" for c in Condition.objects.filter(specialization=Specialization.objects.get(pk=value))]
        data['procedures'] = ["<option value='"+str(p.id)+"'>"+str(p)+"</option>" for p in Procedure.objects.filter(specialization=Specialization.objects.get(pk=value))]
        return HttpResponse(json.dumps(data), content_type="application/json")


def get_practice_names_ajax(request):
    if request.is_ajax():
        practice_q = request.GET.get('q', '')
        practice_type = request.GET.get('type', '')
        practice_names = Practice.practice_objects.practice_names(
            name=practice_q,
            p_type=practice_type
        )
        suggestions = [
            {
                'id': result.id,
                'text': result.practice_location.name
            }
            for result in practice_names
        ]
        the_data = json.dumps(suggestions)
        return HttpResponse(the_data, content_type='application/json')


def get_practice_details_ajax(request):
    if request.is_ajax():
        practice_id = request.GET.get('practice_id', '')
        practice_location = Practice.objects.get(
            id=practice_id
        ).practice_location
        data = json.dumps(
            {
                'address': practice_location.clinic_address,
                'city': practice_location.area.city.id,
                'area_id': practice_location.area.id,
                'area_name': practice_location.area.name,
                'contact_number': practice_location.contact_number
            }
        )
        return HttpResponse(data, content_type='application/json')
