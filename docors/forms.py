from django import forms
from django.forms.widgets import Input, HiddenInput

class doctors_form(forms.Form):

	q = forms.CharField(max_length=100, required=False, label="Doctor", widget=forms.TextInput(attrs={'placeholder': 'Doctor Name, Specialty, Condition or Procedure', 'class':'doc-typeahead'}))

class speciality_form(forms.Form):

	spec = forms.CharField(max_length=100, required=True, label="Specialty", widget=forms.TextInput(attrs={'placeholder': 'eg. Child SPecialist', 'class':'typeahead spec_typeahead'}))
	area = forms.CharField(max_length=100, required=True, label="Area", widget=forms.TextInput(attrs={'placeholder': 'eg. Faisal Town', 'class':'typeahead area_typeahead'}))

class advanced_form(forms.Form):

	RADIUS_CHOICES = ((10, '10'), (20, '20'), (30, '30'), (40, '40'),)
	DAYS = (('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'),('6', 'Saturday'),('7', 'Sunday'),)

	spec = forms.CharField(max_length=100, required=True, label="Specialty", widget=forms.TextInput(attrs={'placeholder': 'eg. Child SPecialist', 'class':'typeahead spec_typeahead'}))
	radius = forms.ChoiceField(choices = RADIUS_CHOICES, label="Radius (KM)", initial='10', required = True)
	day = forms.ChoiceField(choices = DAYS, label = "Day", initial='1', required = True)
	lon = forms.CharField(label='Physical longitude.', widget=forms.HiddenInput(), required=False)
	lat = forms.CharField(label='Physical latitude.', widget=forms.HiddenInput(), required=False)