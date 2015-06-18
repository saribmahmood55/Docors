from django.db import models
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField

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

class ConditionManager(models.Manager):
    def get_slug(self, name):
        return super(ConditionManager, self).get(name=name)

    def get_conditions(self, specialization):
        return super(ConditionManager, self).filter(specialization=specialization)

    def get_specialization(self, condition):
        return super(ConditionManager, self).get(name=condition)

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

class ProcedureManager(models.Manager):
    def get_slug(self, name):
        return super(ProcedureManager, self).get(name=name)

    def get_procedures(self, specialization):
        return super(ProcedureManager, self).filter(specialization=specialization)

    def get_specialization(self, procedure):
        return super(ProcedureManager, self).get(name=procedure)

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

class PractitionerManager(models.Manager):

    def practitioner_slug(self, slug):
        return super(PractitionerManager, self).get(slug=slug)

    def practitioner_suggest(self, name):
        return super(PractitionerManager, self).filter(name__icontains=name, status=True).values_list('name', flat=True)


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
    conditions = models.ManyToManyField(Condition)
    procedures = models.ManyToManyField(Procedure)

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