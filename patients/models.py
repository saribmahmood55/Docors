from django.db import models
from django.conf import settings
from practitioner.models import Specialization, Practitioner
from practice.models import City
from docorsauth.models import docorsUser


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
    GENDER_CHOICES = ( ('M', 'Male'),('F', 'Female'), ('N', 'Prefer not to disclose'))
    AGE_GROUPS = (('10', '10-14'), ('15', '15-19'), ('20', '20-24'), ('25', '25-29'), ('30', '30-34'), ('35', '35-39'),('40', '40-44'),('45', '45-49'), ('50', '50-54'), ('55', '55-59'), ('60', '60-64'), ('65', '65-69'), ('70', '70-74'),('75', '75-79'),('80', '80-84'), ('85', '85+'),)
    cell_number = models.CharField(max_length=20, help_text="Please use the following format: 03215555555",null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, help_text="Please select gender.", null=True, blank=True)
    age_group = models.CharField(max_length=2, choices=AGE_GROUPS, help_text="Please select appropriate age group." ,null=True, blank=True)
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