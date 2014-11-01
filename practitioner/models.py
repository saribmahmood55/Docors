from django.db import models
from django.db.models import Q
from autoslug import AutoSlugField

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique = True)
    

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Specialities"


#Custom Manager
class PractitionerManager(models.Manager):

    def practitioner_slug(self, slug):
        return super(PractitionerManager, self).get(slug=slug)


class Practitioner(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', unique = True)
    credentials = models.TextField()
    achievements = models.TextField(null=True)
    experience = models.PositiveIntegerField(default=0, help_text="Number of years", null=True)
    message = models.TextField(max_length=140,null=True, blank=True)
    status = models.BooleanField(default=False)
    specialities = models.ManyToManyField(Specialization)
    modified = models.DateTimeField(auto_now=True)

    #Manager
    objects = models.Manager()
    prac_objects = PractitionerManager()
    
    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"


class PractiseLocation(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique = True)
    clinic_address = models.TextField()
    city = models.ForeignKey(City)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    def __unicode__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "Practise Locations"


#Custom Manager
class PractiseManager(models.Manager):

    def practise_detail(self, slug):
        practise = super(PractiseManager, self).filter(practitioner__slug=slug)
        return practise


    # Search request handling
    def practise_details(self, city, name, speciality, experience, day):
        result = {}
        query = super(PractiseManager, self).filter(practise_location__city__slug=city)
        query = query.distinct('practitioner')
        #filter name
        if day != None:
            query.filter(practisetiming__practitioner__slug=speciality, )
        if name != None and speciality == None:
            query = query.filter(practitioner__name__icontains=name)
            print name
        #filter Speciality
        if speciality != None :
            query = query.filter(practitioner__specialities__slug=speciality)
            #filter name and specialty
            if name != None:
                query = query.filter(practitioner__name__icontains=name)
            #filter experienced
            if experience >= 0:
                query = query.filter(practitioner__experience__gte=experience)
        #filter day
        if day != None:
            query = query.filter(practitioner__specialities__slug=speciality).distinct('practitioner')
        result['practise_list'] = query
        return result


class Practise(models.Model):
    PRACTISE_CHOICES = (
        ('P', 'Private Clininc'),
        ('H', 'Hospital'),
    )
    practise_type = models.CharField(max_length=1, choices=PRACTISE_CHOICES, help_text="Practise Type")
    practise_location = models.ForeignKey(PractiseLocation)
    practitioner = models.ForeignKey(Practitioner)
    contact_number = models.CharField(max_length=100)
    checkup_fee = models.PositiveIntegerField()
    services = models.TextField(null=True, blank=True)
    appointments_only = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()
    practise_objects = PractiseManager()

    def __unicode__(self):
        return self.practise_location.name

    class Meta:
        verbose_name_plural = "Practise"


#Custom Manager
class PractiseTimingManager(models.Manager):
    def practise_timings(self, pr_slug, p_slug):
        practise_timings = super(PractiseTimingManager, self).filter(practise_location__slug=pr_slug, practitioner__slug=p_slug).order_by('pk')
        return practise_timings    

    def spec_day_timing(self, spec, day):
        practise_timings = super(PractiseTimingManager, self).filter(practitioner__specialities__slug=spec, day=day).order_by('pk')
        return practise_timings

class PractiseTiming(models.Model):
    DAY = (
        ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'),('Sat', 'Saturday'),('Sun', 'Sunday'),
        )
    TIME = (
        ('8', '08:00am'),('8.5', '08:30am'),('9', '09:00am'),('9.5', '09:30am'),('10', '10:00am'),('10.5', '10:30am'),('11', '11:00am'),('11.5', '11:30am'),
        ('12', '12:00pm'),('12.5', '12:30pm'),('13', '01:00pm'),('13.5', '01:30pm'),('14', '02:00pm'),('14.5', '02:30am'),('15', '03:00pm'),('15.5', '03:30pm'),
        ('16', '04:00pm'),('16.5', '04:30pm'),('17', '05:00pm'),('17.5', '05:30pm'),('18', '06:00pm'),('18.5', '06:30pm'),('19', '07:00pm'),('19.5', '07:30pm'),
        ('20', '08:00pm'),('20.5', '08:30pm'),('21', '09:00pm'),('21.5', '09:30pm'),('22', '10:00pm'),('22.5', '10:30pm'),('23', '11:00pm'),('23.5', '11:30pm'),
        ('0', '12:00am'),('0.5', '12:30am'), ('1', "01:00am"),('2', '02:00am'), ('2.5', "02:30am")
        )
    
    practitioner = models.ForeignKey(Practitioner)
    practise_location = models.ForeignKey(PractiseLocation)
    day = models.CharField(max_length=3, choices=DAY, help_text="Select Day.")
    start_time = models.CharField(max_length=5, choices=TIME, help_text="Select starting Time for Clininc.")
    end_time = models.CharField(max_length=5, choices=TIME, help_text="Select ending Time for Clininc.")

    #Custom Managers
    objects = models.Manager()
    pt_objects = PractiseTimingManager()

    def __unicode__(self):
        return self.practitioner.name

    class Meta:
        verbose_name_plural = "Practise Timings"