from django import forms
from django.forms.widgets import Input, HiddenInput
from django.forms.formsets import BaseFormSet
from practitioner.tasks import confirmation_mail
from practitioner.models import Practitioner, Claim, UpdateInfo
from practice.models import City, CheckupFee, Area
from practice.models import Practice, PracticeLocation, PracticeTiming
from reviews.models import Answer, Comment
import re


class Html5EmailInput(Input):
    input_type = 'email'


class BasePracticeFormSet(BaseFormSet):
    def save(self, practitioner, extraPracticeTimings):
        for idx, form in enumerate(self.forms):
            if form not in self.deleted_forms:
                form.save(practitioner, extraPracticeTimings[idx])
            else:
                print "form is deleted"


class PracticeForm(forms.Form):

    Practice_CHOICES = (
        (u'P', u'Clinic/Residence'),
        (u'H', u'Hospital'),
        (u'M', u'Medical Complex'),
    )
    Appointment_Option = (
        (u'True', u'Strictly on Appointment.'),
        (u'False', u'Checkup allowed on Waiting.'),
    )
    DAYS = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )

    practice_exists = forms.CharField(
        required=True,
        label='Exists',
        widget=HiddenInput()
    )
    practice_name = forms.CharField(
        required=True,
        label='Name.',
        widget=HiddenInput()
    )
    address = forms.CharField(
        max_length=500,
        required=True,
        label='Street address.',
        widget=forms.Textarea(
            attrs={
                'data-error': 'Please provide a valid address',
                'placeholder': 'eg. 82-XX, DHA',
                'rows': '1'
            }
        )
    )
    practice_photo = forms.ImageField(
        label='Photo of your clinic outer space.',
        required=False
    )
    city = forms.ChoiceField(
        choices=[(r.id, r) for r in City.objects.order_by('pk')],
        label="City.",
        required=True
    )
    area = forms.CharField(widget=HiddenInput(), required=True, label="Area.")
    lon = forms.CharField(
        label='Physical longitude.',
        widget=forms.HiddenInput(),
        required=False
    )
    lat = forms.CharField(
        label='Physical latitude.',
        widget=forms.HiddenInput(),
        required=False
    )
    # Practice
    practice_type = forms.ChoiceField(
        choices=Practice_CHOICES,
        label="Practice type",
        initial='3',
        required=True
    )
    contact_number = forms.CharField(
        max_length=100,
        label="Contact number(s)",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'eg. 0423585xxxx, 03214567xxx'
            }
        ),
        required=True
    )
    checkup_fee = forms.ChoiceField(
        choices=[(fee.id, fee) for fee in CheckupFee.objects.all()],
        label='Checkup fee (pkr).'
    )
    appointment = forms.ChoiceField(
        required=True,
        choices=Appointment_Option,
        label="Appointment criteria."
    )
    # Timings
    day = forms.ChoiceField(
        choices=DAYS,
        label="Day",
        initial='1',
        required=True
    )
    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'placeholder': 'hh:mm (24h format)'
            },
            format='%H:%M'),
        label="Start time."
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'placeholder': 'hh:mm (24h format)'
            },
            format='%H:%M'
        ),
        label="End time."
    )

    def save(self, practitioner, extraTimings):
        practice_form = self
        if practice_form.cleaned_data['practice_exists'] != "1":
            practice_name = practice_form.cleaned_data['practice_name']
            address = practice_form.cleaned_data['address']
            photo = practice_form.cleaned_data['practice_photo']
            area_id = practice_form.cleaned_data['area']
            area = Area.objects.get(pk=area_id)
            lon = practice_form.cleaned_data['lon']
            lat = practice_form.cleaned_data['lat']
            contact_number = practice_form.cleaned_data['contact_number']

            # create PracticeLocation
            practice_location = PracticeLocation(
                name=practice_name,
                contact_number=contact_number,
                photo=photo,
                clinic_address=address,
                area=area,
                lon=lon,
                lat=lat)
            practice_location.save()
        else:
            practice_id = practice_form.cleaned_data['practice_name']
            practice_location = PracticeLocation.objects.get(id=practice_id)

        # Practice
        practice_type = practice_form.cleaned_data['practice_type']
        checkup_fee_id = practice_form.cleaned_data['checkup_fee']
        checkup_fee = CheckupFee.objects.get(pk=checkup_fee_id)
        appointment = practice_form.cleaned_data['appointment']

        # Create Practice
        practice = Practice(
            practice_type=practice_type,
            practice_location=practice_location,
            practitioner=practitioner,
            fee=checkup_fee,
            appointments_only=appointment
        )
        practice.save()

        # PracticeTiming
        day = int(practice_form.cleaned_data['day'])
        start_time = practice_form.cleaned_data['start_time']
        end_time = practice_form.cleaned_data['end_time']
        # Create PracticeTiming
        pt = PracticeTiming(
            practice=practice,
            day=day,
            start_time=start_time,
            end_time=end_time
        )
        pt.save()

        # Extra Timings
        for key, day in enumerate(extraTimings["day"]):
            pt = PracticeTiming(
                practice=practice,
                day=int(day),
                start_time=extraTimings["start_time"][key],
                end_time=extraTimings["end_time"][key]
            )
            pt.save()

        # send email
        email_domain = re.search("@[\w.]+", practitioner.email).group()
        if email_domain[1::] != "doctorsinfo.pk":
            email_details = {
                'name': practitioner.full_name,
                'email': practitioner.email,
                'slug': practitioner.slug
            }
            confirmation_mail.delay(email_details)
        return practice


class ClaimPractitionerForm(forms.ModelForm):

    class Meta:
        model = Claim
        fields = ['email', 'pmdc_no']

    def save(self, slug):
        claim = super(ClaimPractitionerForm, self).save(commit=False)
        claim.practitioner = Practitioner.objects.get(slug=slug)
        claim.save()
        return claim


class UpdateInfoForm(forms.ModelForm):

    class Meta:
        model = UpdateInfo
        fields = ['incorrect_info', 'correct_info', 'comments']

    def save(self, ip, slug):
        update = super(UpdateInfoForm, self).save(commit=False)
        update.ip = ip
        update.practitioner = Practitioner.objects.get(slug=slug)
        update.save()
        return update


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Practitioner
        fields = [
            'conditions',
            'procedures',
            'experience',
            'message',
            'achievements'
        ]


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        exclude = ()
        widgets = {
            'answer1': forms.HiddenInput(),
            'answer2': forms.HiddenInput(),
            'answer3': forms.HiddenInput(),
            'answer4': forms.HiddenInput(),
            'answer5': forms.HiddenInput(),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }
