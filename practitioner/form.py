# flake8: noqa
from django import forms
from django.forms.widgets import Input
from practitioner.models import *
from practice.models import City,CheckupFee

class Html5EmailInput(Input): 
    input_type = 'email'

class PractitionerForm(forms.Form):

	error_css_class = 'has-error'
	required_css_class = 'required'

	PHYSICIAN_CHOICES = ( ('1', 'Trainee'), ('2', 'Specialist'),)
	GENDER = ( ('M', 'Male'),('F', 'Female'),)
	YEARS = [(year, year) for year in range(1935, 1991)]
	Practice_CHOICES = ((u'P', u'Clinic/Residence'),(u'H', u'Hospital'),(u'M', u'Medical Complex'),)
	Appointment_Option = ((u'True', u'Strictly on Appointment.'),(u'False', u'Checkup allowed on Waiting.'),)
	DAYS = (('1', 'Monday'), ('2', 'Tuesday'), ('3', 'Wednesday'), ('4', 'Thursday'), ('5', 'Friday'),('6', 'Saturday'),('7', 'Sunday'),)
	TIME = (('0', '07:00am'), ('1', '07:30am'),('2', '08:00am'),('3', '08:30am'),('4', '09:00am'),('5', '09:30am'),('6', '10:00am'),('7', '10:30am'),('8', '11:00am'),('9', '11:30am'),('10', '12:00pm'),('11', '12:30pm'),('12', '01:00pm'),('13', '01:30pm'),('14', '02:00pm'),('15', '02:30am'),('16', '03:00pm'),('17', '03:30pm'),('18', '04:00pm'),('19', '04:30pm'),('20', '05:00pm'),('21', '05:30pm'),('22', '06:00pm'),('23', '06:30pm'),('24', '07:00pm'),('25', '07:30pm'),('26', '08:00pm'),('27', '08:30pm'),('28', '09:00pm'),('29', '09:30pm'),('30', '10:00pm'),('31', '10:30pm'),('32', '11:00pm'),('33', '11:30pm'),('34', '12:00am'), ('35', '12:30am'), ('36', "01:00am"), ('37', '02:00am'), ('38', "02:30am"),)
	
	#practitioner
	practitioner_name = forms.CharField(max_length=100, required=True, label="Name", widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
	practitioner_gender = forms.ChoiceField(choices=GENDER, label="Gender", initial='M', required=True)
	year_of_birth = forms.ChoiceField(choices=YEARS, label="Year of Birth", initial="1900", required=True)
	email = forms.EmailField(label= "Email", max_length=75, required=True, widget=Html5EmailInput(attrs={'placeholder':'example@gmail.com'}))
	physician_type = forms.ChoiceField(choices = PHYSICIAN_CHOICES, label="Physician type", initial='1', required = True)
	credentials = forms.CharField(max_length=500, required=True, label="Credentials.", widget=forms.TextInput(attrs={'data-provide':'typeahead','placeholder':'Credentials'}))
	achievements = forms.CharField(max_length=800, required=False, label='Achievements.', widget=forms.Textarea(attrs={'placeholder': 'education, training & achievements','rows':'1'}))
	experience = forms.IntegerField(label='Experience (years).', initial='0', widget=forms.NumberInput(attrs={'min':'0'}), required=True)
	message = forms.CharField(max_length=160, required=False, label='Short message for patients.', widget=forms.TextInput(attrs={'placeholder': 'eg. available, out of country till..'}))
	specialities = forms.ChoiceField(choices = [(r.id, r) for r in Specialization.objects.order_by('name')], label='Speciality.', required = True)
	conditions = forms.ChoiceField(choices = [(r.id, r) for r in Condition.objects.filter(specialization=Specialization.objects.order_by('name')[0])], widget=forms.Select(attrs={'multiple':'multiple'}), label='Conditions.', required = True)
	procedures = forms.ChoiceField(choices = [(r.id, r) for r in Procedure.objects.filter(specialization=Specialization.objects.order_by('name')[0])], widget=forms.Select(attrs={'multiple':'multiple'}), label='Procedures.', required = True)
	#Practice Location
	practice_name = forms.CharField(max_length=50, required=True, label='Name.', widget=forms.TextInput(attrs={'data-error':'Please provide a valid name','placeholder': 'eg. Adil Hospital'}))
	address = forms.CharField(max_length=500, required=True, label='Street address.', widget=forms.Textarea(attrs={'data-error':'Please provide a valid address','placeholder': 'eg. 82-XX, DHA','rows':'1'}))
	photo = forms.ImageField(label='Photo of your clinic outer space.', required=False)
	city = forms.ChoiceField(choices = [(r.id, r) for r in City.objects.order_by('pk')], label="City.", required = True)
	lon = forms.CharField(label='Physical longitude.', widget=forms.HiddenInput(), required=False)
	lat = forms.CharField(label='Physical latitude.', widget=forms.HiddenInput(), required=False)
	#Practice
	practice_type = forms.ChoiceField(choices = Practice_CHOICES, label="Practice type", initial='3', required = True)
	contact_number = forms.CharField(max_length=100, label="Contact number(s)",widget=forms.TextInput(attrs={'placeholder': 'eg. 0423585xxxx, 03214567xxx'}), required=True)
	checkup_fee = forms.ChoiceField(choices = [(fee.id, fee) for fee in CheckupFee.objects.all()], label='Checkup fee (pkr).')
	appointment = forms.ChoiceField(required=True, choices = Appointment_Option, label="Appointment criteria.")
	#Timings
	day_from = forms.ChoiceField(choices = DAYS, label = "From day", initial='1', required = True)
	day_to = forms.ChoiceField(choices = DAYS, label = "To day", initial='5', required = True)
	start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label = "Start time.")
	end_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), label = "End time.")
