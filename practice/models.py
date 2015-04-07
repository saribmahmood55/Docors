from django.db import models
from practitioner.models import *
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.contrib.gis import measure
from django.core.urlresolvers import reverse

class City(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique = True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"

class CheckupFee(models.Model):
    amount = models.PositiveSmallIntegerField()
    
    def __unicode__(self):
        return str(self.amount)
    
    class Meta:
        verbose_name_plural = "CheckupFee"

class PracticeLocation(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique = True)
    contact_number = models.CharField(max_length=150, null=True, blank=True)
    photo = ImageField(upload_to='practice/', blank=True, null=True)
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

    
    # Search by Practitioner Name
    def practitioner_name(self, name):
        result = {}
        result['practice_list'] = super(PracticeManager, self).filter(practitioner__name__icontains=name, practitioner__status=True).distinct('practitioner')
        return result

    # Basic Search request handling
    def practice_lookup(self, city, spec, dist, lon, lat, name, day, wait):
        result, query = {}, None
        if lon == '' and lat == '':
            query = super(PracticeManager, self).filter(practitioner__specialities__slug=spec, practitioner__status=True, practice_location__city__slug=city).distinct('practitioner')
            if name != '':
                query = query.filter(practitioner__name__icontains=name)
            if day != '':
                query = query.filter(practicetiming__day=day).distinct('practitioner')
    		if wait == 1:
    			query = query.filter(appointments_only=False)
        else:
        	current_point = geos.fromstr("POINT(%s %s)" % (lon, lat))
    		distance_from_point = {'km': dist}
    		query = Practice.gis.filter(location__distance_lte=(current_point, measure.D(**distance_from_point)))
    		query = query.distance(current_point).order_by('distance')
    		query = query.filter(practitioner__specialities__slug=spec, practitioner__status=True)
    		#spatial name search
    		if name != '':
    			query = query.filter(practitioner__name__icontains=name)
    		if day != '':
    			query = query.filter(practicetiming__day=day).distinct('practitioner')
    			query = query.distance(current_point).order_by('practitioner')
    		if wait == 1:
    			query = query.filter(appointments_only=False)
        
        result['practice_list'] = query
        return result
    # Recent Search Handling
    def practice_recentlookups(self, city, spec):
        result, query = {}, None
        query = super(PracticeManager, self).filter(practitioner__specialities__slug=spec, practitioner__status=True, practice_location__city__slug=city).distinct('practitioner')
        result['practice_list'] = query
        return result


class Practice(models.Model):
    Practice_CHOICES = (
        ('P', 'Private Clinic/Residence'),
        ('H', 'Hospital'),
        ('M', 'Medical Complex'),
    )
    practice_type = models.CharField(max_length=1, choices=Practice_CHOICES, help_text="Practice Type")
    practice_location = models.ForeignKey(PracticeLocation)
    practitioner = models.ForeignKey(Practitioner)
    fee = models.ForeignKey(CheckupFee, null=True, blank=True)
    services = models.TextField(null=True, blank=True)
    appointments_only = models.BooleanField(default=True)
    location = gis_models.PointField(geography=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)
    
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

    def get_absolute_url(self):
        return reverse('practitioner', args=[self.practitioner.slug])

#Custom Manager
class PracticeTimingManager(models.Manager):
    def practice_timings(self, pr_slug, p_slug):
        practice_timings = super(PracticeTimingManager, self).filter(practice__practice_location__slug=pr_slug, practitioner__slug=p_slug).order_by('pk')
        return practice_timings    

    def spec_day_timing(self, spec, day):
        practice_timings = super(PracticeTimingManager, self).filter(practitioner__specialities__slug=spec, day=day).order_by('pk')
        return practice_timings

class PracticeTiming(models.Model):
    DAYS = (('1', 'Mon'), ('2', 'Tue'), ('3', 'Wed'), ('4', 'Thu'), ('5', 'Fri'),('6', 'Sat'),('7', 'Sun'),)
    
    practitioner = models.ForeignKey(Practitioner)
    practice = models.ForeignKey(Practice)
    day = models.CharField(max_length=1, choices=DAYS, help_text="Select Day.")
    start_time = models.TimeField(help_text="Select starting Time for Clininc.", auto_now_add=False, null=True, blank=True)
    end_time = models.TimeField(help_text="Select ending Time for Clininc.", auto_now_add=False, null=True, blank=True)

    #Custom Managers
    objects = models.Manager()
    pt_objects = PracticeTimingManager()

    def __unicode__(self):
        return self.practitioner.name

    class Meta:
        verbose_name_plural = "Practice Timings"

class RecentSearch(models.Model):
    city = models.ForeignKey(City)
    speciality = models.ForeignKey(Specialization)
    hit_count = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return "%s in %s" % (self.speciality.name, self.city.name)
    
    class Meta:
        verbose_name_plural = "Recent Searches"
