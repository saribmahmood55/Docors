from django.db import models
from practitioner.models import *
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField
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

    
    # Search by Practitioner Name
    def practitioner_name(self, name):
        result = {}
        result['practice_list'] = super(PracticeManager, self).filter(practitioner__name__icontains=name, practitioner__status=True)
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
        ('P', 'Private Clininc/Residence'),
        ('H', 'Hospital'),
    )
    practice_type = models.CharField(max_length=1, choices=Practice_CHOICES, help_text="Practice Type")
    practice_location = models.ForeignKey(PracticeLocation)
    practitioner = models.ForeignKey(Practitioner)
    practice_photo = ImageField(upload_to='practice/', blank=True, null=True)
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
    DAYS = (('1', 'Mon'), ('2', 'Tue'), ('3', 'Wed'), ('4', 'Thu'), ('5', 'Fri'),('6', 'Sat'),('7', 'Sun'),)
    TIME = (('0', '07:00am'), ('1', '07:30am'),('2', '08:00am'),('3', '08:30am'),('4', '09:00am'),('5', '09:30am'),('6', '10:00am'),('7', '10:30am'),('8', '11:00am'),('9', '11:30am'),('10', '12:00pm'),('11', '12:30pm'),('12', '01:00pm'),('13', '01:30pm'),('14', '02:00pm'),('15', '02:30am'),('16', '03:00pm'),('17', '03:30pm'),('18', '04:00pm'),('19', '04:30pm'),('20', '05:00pm'),('21', '05:30pm'),('22', '06:00pm'),('23', '06:30pm'),('24', '07:00pm'),('25', '07:30pm'),('26', '08:00pm'),('27', '08:30pm'),('28', '09:00pm'),('29', '09:30pm'),('30', '10:00pm'),('31', '10:30pm'),('32', '11:00pm'),('33', '11:30pm'),('34', '12:00am'), ('35', '12:30am'), ('36', "01:00am"), ('37', '02:00am'), ('38', "02:30am"),)
    
    practitioner = models.ForeignKey(Practitioner)
    practice = models.ForeignKey(Practice)
    day = models.CharField(max_length=1, choices=DAYS, help_text="Select Day.")
    start_time = models.CharField(max_length=2, choices=TIME, help_text="Select starting Time for Clininc.")
    end_time = models.CharField(max_length=2, choices=TIME, help_text="Select ending Time for Clininc.")

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