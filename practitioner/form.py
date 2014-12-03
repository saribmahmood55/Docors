from django import forms
from django.forms.widgets import Input
from captcha.fields import ReCaptchaField
from practitioner.models import *
from practice.models import City

class Html5EmailInput(Input): 
    input_type = 'email'

class PractitionerForm(forms.Form):
	
	Practice_CHOICES = (
		(u'P', u'Private Clininc/Residence'),
		(u'H', u'Hospital'),
		)
	Appointment_Option = (
		(u'True', u'Strictly on Appointment.'),
		(u'False', u'Checkup allowed on Waiting.'),
		)
	DAYS = (
        ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'),('Sat', 'Saturday'),('Sun', 'Sunday'),
        )
	
	TIME = (
        ('7', '07:00am'), ('7.5', '07:30am'),('8', '08:00am'),('8.5', '08:30am'),('9', '09:00am'),('9.5', '09:30am'),('10', '10:00am'),('10.5', '10:30am'),('11', '11:00am'),('11.5', '11:30am'),
        ('12', '12:00pm'),('12.5', '12:30pm'),('13', '01:00pm'),('13.5', '01:30pm'),('14', '02:00pm'),('14.5', '02:30am'),('15', '03:00pm'),('15.5', '03:30pm'),
        ('16', '04:00pm'),('16.5', '04:30pm'),('17', '05:00pm'),('17.5', '05:30pm'),('18', '06:00pm'),('18.5', '06:30pm'),('19', '07:00pm'),('19.5', '07:30pm'),
        ('20', '08:00pm'),('20.5', '08:30pm'),('21', '09:00pm'),('21.5', '09:30pm'),('22', '10:00pm'),('22.5', '10:30pm'),('23', '11:00pm'),('23.5', '11:30pm'),
        ('0', '12:00am'), ('0.5', '12:30am'), ('1', "01:00am"), ('2', '02:00am'), ('2.5', "02:30am"),
        )
	captcha = ReCaptchaField()
	practitioner_name = forms.CharField(max_length=60, required=True)
	email = forms.EmailField(label= "E-mail", max_length=75, required=True, widget=Html5EmailInput())
	credentials = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'MBBS, DABIM, MRCP, FRCP, FRCS, FACP'}))
	achievements = forms.CharField(max_length=600, widget=forms.Textarea)
	experience = forms.IntegerField()
	message = forms.CharField(max_length=160, required=False, widget=forms.TextInput(attrs={'placeholder': 'available, out of country till 10-Feb-2015'}))
	specialities = forms.ChoiceField(choices = [(r.id, r) for r in Specialization.objects.order_by('name')], label = "Select speciality",required = True)
    
    #Practice Location
	practice_name = forms.CharField(max_length=50, required=True)
	address = forms.CharField(max_length=500,required=True, widget=forms.Textarea(attrs={'placeholder': '82-XX, DHA'}))
	city = forms.ChoiceField(choices = [(r.id, r) for r in City.objects.order_by('pk')], label = "Select speciality",required = True)
	lon = forms.FloatField()
	lat = forms.FloatField()
    
    #Practice
	practice_type = forms.ChoiceField(choices = Practice_CHOICES, label = "Practice Choice", initial='3', required = True)
	contact_number = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': '04235100000 03214000111'}))
	checkup_fee = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '1500'}))
	services = forms.CharField(max_length=500, widget=forms.Textarea)
	appointments_only = forms.ChoiceField(required=True, choices = Appointment_Option, )
    
    #Timings
	day1 = forms.ChoiceField(choices = DAYS, label = "Day", initial='3', required = True)
	day2 = forms.ChoiceField(choices = DAYS, label = "Day", initial='3', required = True)
	start_time = forms.ChoiceField(choices = TIME, label = "start Time", required = True)
	end_time = forms.ChoiceField(choices = TIME, label = "End Time", required = True)