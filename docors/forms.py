# flake8: noqa
from django import forms
from django.forms.widgets import Input, HiddenInput
from practitioner.models import Specialization
from practice.models import Area, City

class doctors_form(forms.Form):

	q = forms.CharField(max_length=100, required=False, label="Doctor", widget=forms.TextInput(attrs={'placeholder': 'Doctor Name, Specialty, Condition or Procedure', 'class':'doc-typeahead'}))

class speciality_form(forms.Form):

	spec = forms.ChoiceField(choices = [(r.id, r.human_name) for r in Specialization.objects.order_by('name')], label='Speciality.', required = True)
	area = forms.ChoiceField(choices = [(r.id, r.name) for r in Area.objects.filter(city=City.objects.get(name='Lahore'))], label='Area.', required = True)

class advanced_form(forms.Form):

	RADIUS_CHOICES = ((1, '1'), (2, '2'), (5, '5'), (10, '10'), (15, '15'), (20, '20'),)
	DAYS = (('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'),('6', 'Saturday'),('7', 'Sunday'),)

	spec_adv = forms.ChoiceField(choices = [(r.id, r.human_name) for r in Specialization.objects.order_by('name')], label='Speciality.', required = True)
	lon = forms.CharField(label='Physical longitude.', widget=forms.HiddenInput(), required=False)
	lat = forms.CharField(label='Physical latitude.', widget=forms.HiddenInput(), required=False)
	radius = forms.ChoiceField(choices = RADIUS_CHOICES, label="Radius (KM)", initial='2', required = True)
	day = forms.ChoiceField(choices = DAYS, label = "Day", initial='1', required = True)