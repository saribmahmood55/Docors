# flake8: noqa
from django.db import models
from django.conf import settings
from practitioner.models import Specialization, Practitioner
from practice.models import City
from docorsauth.models import docorsUser
from django.core.validators import MaxValueValidator, MinValueValidator


#customManager
class SubscriptionManager(models.Manager):

    def subscription_email_details(self, email, practitioner):
        return super(SubscriptionManager, self).filter(email=email, practitioner=practitioner)

    def subscription_mobile_details(self, mobile, practitioner):
        return super(SubscriptionManager, self).filter(cell_number=mobile, practitioner=practitioner)

    def subscription_both_details(self, email, mobile, practitioner):
        return super(SubscriptionManager, self).filter(email=email, cell_number=mobile, practitioner=practitioner)


class Subscription(models.Model):
    cell_number = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField(max_length=35, blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner)


    objects = models.Manager()
    subscription_objects = SubscriptionManager()

    def __str__(self):
        return self.practitioner.name

    class Meta:
        verbose_name_plural = 'Subscriptions'


#customManager
class PatientManager(models.Manager):

    def patient_details(self, email):
        return super(PatientManager, self).get(email=email)

    def registered_patient(self, email):
        return super(PatientManager, self).filter(email=email)

    def get_city(self, email):
        return super(PatientManager, self).get(email=email).city


class Patient(docorsUser):
    
    cell_number = models.BigIntegerField(
        unique=True, null=True, blank=True,
        validators=[
            MaxValueValidator(
                3500000000,
                message="Please enter a valid mobile phone number e.g. "
                "03001234567"),
            MinValueValidator(
                3000000000,
                message="Please enter a valid mobile phone number e.g. "
                "03001234567")],
        help_text='Mobile phone number e.g. 03001234567'
    )
    interested_specialities = models.ManyToManyField(Specialization, blank=True)
    favt_practitioner = models.ManyToManyField(Practitioner, blank=True)
    city = models.ForeignKey(City, default=1)

    objects = models.Manager()
    patient_objects = PatientManager()

    class Meta:
        verbose_name_plural = 'Patients'

    def patient_name(self):
        return self.full_name

    def __str__(self):
        return self.email