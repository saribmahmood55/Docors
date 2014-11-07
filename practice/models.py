from django.db import models
from practitioner.models import *
from django.db.models import Q
from autoslug import AutoSlugField
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.contrib.gis import measure


class City(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"


class PracticeLocation(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique = True)
    clinic_address = models.TextField()
    city = models.ForeignKey(City)
    lon = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)


    def get_location(self):
        # Remember, longitude FIRST!
        return Point(self.lon, self.lat)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Practice Locations"


#Custom Manager
class PracticeManager(models.Manager):

    def practice_detail(self, slug):
        practice = super(PracticeManager, self).filter(practitioner__slug=slug)
        return practice

    def nearby_practice(self, speciality, dist, lon, lat):
    	result = {}
    	print 'spatial'
    	current_point = geos.fromstr("POINT(%s %s)" % (lon, lat))
    	distance_from_point = {'km': dist}
    	practice = Practice.gis.filter(location__distance_lte=(current_point, measure.D(**distance_from_point)))
    	practice = practice.distance(current_point).order_by('distance')
    	practice = practice.filter(practitioner__specialities__slug=speciality)
    	result['practice_list'] = practice
        return result


    # Search request handling
    def practice_lookup(self, city, speciality, experience, name, day):
        result, query = {}, None
        if city and speciality:
        	query = super(PracticeManager, self).filter(practitioner__specialities__slug=speciality , practice_location__city__slug=city).distinct('practitioner')
        else:
        	query = super(PracticeManager, self).filter(Q(practitioner__specialities__slug=speciality) | Q(practice_location__city__slug=city)).distinct('practitioner')
        
        #filter name
        if name != '':
        	query = query.filter(practitioner__name__icontains=name)

        #filter day
        if day != '':
        	query = query.filter(practicetiming__day=day).distinct('practitioner')
        
        '''
        #filter experienced
        if experience >= 0:
                query = query.filter(practitioner__experience__gte=experience)
        '''
        
        result['practice_list'] = query
        return result


class Practice(models.Model):
    Practice_CHOICES = (
        ('P', 'Private Clininc'),
        ('H', 'Hospital'),
    )
    practice_type = models.CharField(max_length=1, choices=Practice_CHOICES, help_text="Practice Type")
    practice_location = models.ForeignKey(PracticeLocation)
    practitioner = models.ForeignKey(Practitioner)
    contact_number = models.CharField(max_length=100)
    checkup_fee = models.PositiveIntegerField()
    services = models.TextField(null=True, blank=True)
    appointments_only = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True)
    location = gis_models.PointField(geography=True, blank=True, null=True)
    
    objects = models.Manager()
    gis = gis_models.GeoManager()
    practice_objects = PracticeManager()

    def __unicode__(self):
        return self.practice_location.slug

    class Meta:
        verbose_name_plural = "Practice"

    def save(self, **kwargs):
    	point = "POINT(%s %s)" % (self.practice_location.lon, self.practice_location.lat)
    	self.location = geos.fromstr(point)
        super(Practice, self).save()


#Custom Manager
class PracticeTimingManager(models.Manager):
    def practice_timings(self, pr_slug, p_slug):
        practice_timings = super(PracticeTimingManager, self).filter(practice__practice_location__slug=pr_slug, practitioner__slug=p_slug).order_by('pk')
        return practice_timings    

    def spec_day_timing(self, spec, day):
        practice_timings = super(PracticeTimingManager, self).filter(practitioner__specialities__slug=spec, day=day).order_by('pk')
        return practice_timings

class PracticeTiming(models.Model):
    DAYS = (
        ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'),('Sat', 'Saturday'),('Sun', 'Sunday')
        )
    TIME = (
        ('7', '07:00am'), ('7.5', '07:30am'),('8', '08:00am'),('8.5', '08:30am'),('9', '09:00am'),('9.5', '09:30am'),('10', '10:00am'),('10.5', '10:30am'),('11', '11:00am'),('11.5', '11:30am'),
        ('12', '12:00pm'),('12.5', '12:30pm'),('13', '01:00pm'),('13.5', '01:30pm'),('14', '02:00pm'),('14.5', '02:30am'),('15', '03:00pm'),('15.5', '03:30pm'),
        ('16', '04:00pm'),('16.5', '04:30pm'),('17', '05:00pm'),('17.5', '05:30pm'),('18', '06:00pm'),('18.5', '06:30pm'),('19', '07:00pm'),('19.5', '07:30pm'),
        ('20', '08:00pm'),('20.5', '08:30pm'),('21', '09:00pm'),('21.5', '09:30pm'),('22', '10:00pm'),('22.5', '10:30pm'),('23', '11:00pm'),('23.5', '11:30pm'),
        ('0', '12:00am'), ('0.5', '12:30am'), ('1', "01:00am"), ('2', '02:00am'), ('2.5', "02:30am")
        )
    
    practitioner = models.ForeignKey(Practitioner)
    practice = models.ForeignKey(Practice)
    day = models.CharField(max_length=3, choices=DAYS, help_text="Select Day.")
    start_time = models.CharField(max_length=5, choices=TIME, help_text="Select starting Time for Clininc.")
    end_time = models.CharField(max_length=5, choices=TIME, help_text="Select ending Time for Clininc.")

    #Custom Managers
    objects = models.Manager()
    pt_objects = PracticeTimingManager()

    def __unicode__(self):
        return self.practitioner.name

    class Meta:
        verbose_name_plural = "Practice Timings"
