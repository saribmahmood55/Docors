# flake8: noqa
from django.db import models
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField
from docorsauth.models import docorsUser

class SpecializationManager(models.Manager):
    def spec_slug(self, slug):
        return super(SpecializationManager, self).get(slug=slug)

    def spec_human_name(self, name):
        return super(SpecializationManager, self).get(human_name=name)

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
        ordering = ('name',)


class FellowshipManager(models.Manager):
    def spec_slug(self, slug):
        return super(FellowshipManager, self).get(slug=slug)


class Fellowship(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization)
    slug = AutoSlugField(populate_from='name', unique = True)

    objects = models.Manager()
    fellow_objects = FellowshipManager()
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Fellowships"
        ordering = ('name',)

class ConditionManager(models.Manager):
    def get_slug(self, name):
        return super(ConditionManager, self).get(name=name)

    def get_conditions(self, specialization):
        return super(ConditionManager, self).filter(specialization=specialization)

    def get_specialization(self, condition):
        return super(ConditionManager, self).get(name=condition)

    def get_condition(self, pk):
        return super(ConditionManager, self).get(pk=pk)

class Condition(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization)
    slug = AutoSlugField(populate_from='name', unique=True)

    objects = models.Manager()
    condition_objects = ConditionManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Conditions'
        ordering = ('name',)

class ProcedureManager(models.Manager):
    def get_slug(self, name):
        return super(ProcedureManager, self).get(name=name)

    def get_procedures(self, specialization):
        return super(ProcedureManager, self).filter(specialization=specialization)

    def get_specialization(self, procedure):
        return super(ProcedureManager, self).get(name=procedure)

    def get_procedure(self, pk):
        return super(ProcedureManager, self).get(pk=pk)

class Procedure(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.ForeignKey(Specialization)
    slug = AutoSlugField(populate_from='name', unique=True)

    objects = models.Manager()
    procedure_objects = ProcedureManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Procedures'
        ordering = ('name',)

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
        ordering = ('name',)

class PractitionerManager(models.Manager):

    def practitioner_slug(self, slug):
        return super(PractitionerManager, self).get(slug=slug)

    def practitioner_suggest(self, name):
        return super(PractitionerManager, self).filter(name__icontains=name, status=True).values_list('name', flat=True)


class Practitioner(docorsUser):
    PHYSICIAN_CHOICES = [('0', 'General Physician'), ('1', 'Trainee'), ('2', 'Specialist'),]

    physician_type = models.CharField(max_length=1, choices=PHYSICIAN_CHOICES, null=True)
    photo = ImageField(upload_to='practitioner/', blank=True, null=True)
    experience = models.PositiveIntegerField(help_text="Number of years", default=0)
    achievements = models.TextField(null=True, blank=True)    
    message = models.CharField(max_length=140, null=True, blank=True)
    degrees = models.ManyToManyField(Degree)
    
    # specialities
    specialty = models.ForeignKey(Specialization, null=True, blank=True)
    fellowship = models.ManyToManyField(Fellowship, blank=True)
    completion_year = models.PositiveIntegerField("Fellowship expected in year.", default=0)
    conditions = models.ManyToManyField(Condition, blank=True)
    procedures = models.ManyToManyField(Procedure, blank=True)

    slug = AutoSlugField(populate_from='full_name', unique = True)
    status = models.BooleanField(default=False)
    education_marks = models.PositiveIntegerField(default=0)
    recommendation = models.PositiveIntegerField(default=0)
    not_recommended = models.PositiveIntegerField(default=0)
    review_rating = models.DecimalField(max_digits=2, decimal_places=2, default=0.0)

    #Manager
    objects = models.Manager()
    prac_objects = PractitionerManager()
    
    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Practitioners"
        ordering = ('full_name',)