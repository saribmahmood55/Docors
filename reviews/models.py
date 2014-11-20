from django.db import models
from practitioner.models import Practitioner
from practice.models import *
from patients.models import Patient

# Create your models here.
#custom Manager
class ReviewManager(models.Manager):

    def review(self, review_ID):
        return super(ReviewManager, self).get(pk=review_ID)
    
    def practitioner_reviews(self, slug):
        return super(ReviewManager, self).filter(practitioner__slug=slug).order_by('review_date')

    def patient_reviews(self, user):
        return super(ReviewManager, self).filter(patient__user=user).order_by('review_date')

    def single_review(self, user, slug):
        return super(ReviewManager, self).filter(patient__user=user, practitioner__slug=slug)

class Review(models.Model):
    practitioner = models.ForeignKey(Practitioner)
    patient = models.ForeignKey(Patient)
    post_as_anonymous = models.BooleanField(default=False)
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    up_votes = models.PositiveIntegerField(default=0)
    down_votes = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    review_objects = ReviewManager()

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
    	return self.review_text

class ReviewStatsManager(models.Manager):
    def review(self, review_ID, user):
        return super(ReviewStatsManager, self).filter(review__pk=review_ID, patient__user=user) 

class ReviewStats(models.Model):
    review = models.ForeignKey(Review)
    patient = models.ForeignKey(Patient)
    status = models.IntegerField(default=0)  #0, -1 and +1

    objects = models.Manager()
    prs_objects = ReviewStatsManager()

    class Meta:
        verbose_name_plural = 'Reviews Status'