from django.db import models
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField

class SpecializationManager(models.Manager):
    def spec_slug(self, slug):
        return super(SpecializationManager, self).get(slug=slug)

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    human_name = models.CharField(max_length=100, null=True)
    SEO_name = models.CharField(max_length=100, null=True)
    slug = AutoSlugField(populate_from='name', unique = True)

    objects = models.Manager()
    spec_objects = SpecializationManager()
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specialities"

class DegreeManager(models.Manager):
    def get_degree(self, name):
        return super(DegreeManager, self).get(name=name)

class Degree(models.Model):
    name = models.CharField(max_length=50)
    points = models.PositiveSmallIntegerField(default=0)
    color_code = models.CharField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)

    #Manager
    objects = models.Manager()
    degree_objects = DegreeManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Degrees"

class Service(models.Model):
    condition = models.CharField(max_length=150)
    procedure = models.CharField(max_length=150)
    speciality = models.ForeignKey(Specialization)

    def __unicode__(self):
        return self.procedure

    class Meta:
        verbose_name_plural = "Services"

class PractitionerManager(models.Manager):

    def practitioner_slug(self, slug):
        return super(PractitionerManager, self).get(slug=slug)


class Practitioner(models.Model):
    PHYSICIAN_CHOICES = ( (1, 'Trainee'), (2, 'Specialist'),)
    TITLE = ( (1, 'Dr. '), (2, 'Prof. '), (3, 'Prof. Dr. '),)
    GENDER = ( ('M', 'Male'),('F', 'Female'),)

    title = models.PositiveSmallIntegerField(choices = TITLE, null=True, blank=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    year_of_birth = models.PositiveIntegerField(default=0)
    photo = ImageField(upload_to='practitioner/', blank=True, null=True)
    email = models.EmailField(max_length=75, null=True, blank=True)
    experience = models.PositiveIntegerField(help_text="Number of years")
    physician_type = models.PositiveSmallIntegerField(choices = PHYSICIAN_CHOICES, help_text="Physician type", null=True, blank=True)
    achievements = models.TextField(null=True, blank=True)    
    message = models.TextField(max_length=140, null=True, blank=True)
    degrees = models.ManyToManyField(Degree)
    specialities = models.ManyToManyField(Specialization)
    services = models.ManyToManyField(Service)

    slug = AutoSlugField(populate_from='name', unique = True)
    status = models.BooleanField(default=False)
    education_marks = models.PositiveIntegerField(default=0)
    recommendation = models.PositiveIntegerField(default=0)
    not_recommended = models.PositiveIntegerField(default=0)
    modified = models.DateTimeField(auto_now=True)

    #Manager
    objects = models.Manager()
    prac_objects = PractitionerManager()
    
    def __unicode__(self):
        return self.name