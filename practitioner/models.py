from django.db import models
from autoslug import AutoSlugField

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    human_name = models.CharField(max_length=100, null=True)
    SEO_name = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='name', unique = True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specialities"


class PractitionerManager(models.Manager):

    def practitioner_slug(self, slug):
        return super(PractitionerManager, self).get(slug=slug)


class Practitioner(models.Model):
    PHYSICIAN_CHOICES = ( (1, 'Trainee'), (2, 'Specialist'),)
    TITLE = ( (1, 'Dr. '), (2, 'Prof. '), (3, 'Prof. Dr. '),)

    title = models.PositiveSmallIntegerField(choices = TITLE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=75, null=True, blank=True)
    recommendation = models.PositiveIntegerField(default=0)
    not_recommended = models.PositiveIntegerField(default=0)
    slug = AutoSlugField(populate_from='name', unique = True)
    credentials = models.TextField()
    physician_type = models.PositiveSmallIntegerField(choices = PHYSICIAN_CHOICES, help_text="Physician type", null=True, blank=True)
    achievements = models.TextField(null=True, blank=True)
    experience = models.PositiveIntegerField(help_text="Number of years")
    message = models.TextField(max_length=140, null=True, blank=True)
    status = models.BooleanField(default=False)
    specialities = models.ManyToManyField(Specialization)
    modified = models.DateTimeField(auto_now=True)

    #Manager
    objects = models.Manager()
    prac_objects = PractitionerManager()
    
    def __unicode__(self):
        return self.name