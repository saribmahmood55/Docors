from django.db import models
from django.contrib.auth.models import User
from practitioner.models import Practitioner
from practice.models import *
from patients.models import Patient

# Create your models here.
#custom Manager

class AnswerManager(models.Manager):
    def review(self, review_ID, user):
        return super(AnswerManager, self).filter(review__pk=review_ID, patient__user=user)

class Answer(models.Model):
    answer1 = models.PositiveIntegerField(default=0)
    answer2 = models.PositiveIntegerField(default=0)
    answer3 = models.PositiveIntegerField(default=0)
    answer4 = models.PositiveIntegerField(default=0)
    answer5 = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    answer_objects = AnswerManager()

    def __unicode__(self):
        return "%f" % (self.answer1+self.answer2+self.answer3+self.answer4+self.answer5)

    class Meta:
        verbose_name_plural = 'Answers'

class CommentManager(models.Manager):
    def review(self, review_ID, user):
        return super(CommentManager, self).filter(review__pk=review_ID, patient__user=user)

class Comment(models.Model):
    text = models.CharField(max_length=150)
    agree = models.PositiveIntegerField(default=0)
    disagree = models.PositiveIntegerField(default=0)

    objects = models.Manager()
    comment_objects = CommentManager()

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Comments'

class ReviewManager(models.Manager):

    def review(self, review_ID):
        return super(ReviewManager, self).get(pk=review_ID)
    
    def practitioner_reviews(self, slug):
        return super(ReviewManager, self).filter(practitioner__slug=slug).order_by('timestamp')

    def patient_reviews(self, user):
        return super(ReviewManager, self).filter(patient__user=user).order_by('timestamp')

    def single_review(self, user, slug):
        return super(ReviewManager, self).filter(patient__user=user, practitioner__slug=slug)

class Review(models.Model):
    patient = models.ForeignKey(Patient)
    practitioner = models.ForeignKey(Practitioner)
    answers = models.ForeignKey(Answer, null=True)
    comments = models.ForeignKey(Comment, null=True)
    anonymous = models.NullBooleanField()
    timestamp = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()
    review_objects = ReviewManager()

    class Meta:
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.practitioner.name

class Question(models.Model):
    question1 = models.CharField(max_length=150)
    question2 = models.CharField(max_length=150)
    question3 = models.CharField(max_length=150)
    question4 = models.CharField(max_length=150)
    question5 = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Questions'