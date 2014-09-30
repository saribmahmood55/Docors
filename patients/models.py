from django.db import models
from practitioner.models import Specialization, Practitioner


class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
	    ('F', 'Female'),
	)
    AGE_GROUPS = (
		('0', '0-4'),
		('5', '5-9'),
		('10', '10-14'),
		('15', '15-19'),
		('20', '20-24'),
		('25', '25-29'),
		('30', '30-34'),
		('35', '35-39'),
		('40', '40-44'),
		('45', '45-49'),
		('50', '50-54'),
		('55', '55-59'),
		('60', '60-64'),
		('65', '65-69'),
		('70', '70-74'),
		('75', '75-79'),
		('80', '80-84'),
		('85', '85+'),
	)
    name = models.CharField(max_length=50, help_text='Complete Name')
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    cell_number = models.CharField(max_length=20, help_text='Cell Number. Example: 03215555555')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    age_group = models.CharField(max_length=2, choices=AGE_GROUPS, help_text="Select appropriate age group.",null=True, blank=True)
    interested_specialities = models.ManyToManyField(Specialization, null=True, blank=True)
    favt_practitioner = models.ManyToManyField(Practitioner, null=True, blank=True)
    

    class Meta:
        verbose_name_plural = 'Patients'

    def __str__(self):
    	return self.name


class PractitionerReview(models.Model):
    practitioner = models.ManyToManyField(Practitioner)
    patient = models.ManyToManyField(Patient)
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name_plural = 'Practitioner Reviews'

    def __str__(self):
    	return self.review_text