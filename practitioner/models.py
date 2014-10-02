from django.db import models
from django.contrib.gis.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name


#Custom Managers
class PractitionerManager(models.Manager):
    
    def practitioner_name(self,prac_name):
        return super(PractitionerManager, self).filter(name__icontains=prac_name)

    def practitioner_speciality(self,speciality):
        return super(PractitionerManager, self).filter(specialities__name__icontains=speciality)

    def practitioner_name_and_speciality(self,prac_name,speciality):
        return super(PractitionerManager, self).filter(name__icontains=prac_name,specialities__name__icontains=speciality)

    def practitioner_experienced(self,experience,speciality):
        return super(PractitionerManager, self).filter(experience__gte=experience,specialities__name__icontains=speciality)


class Practitioner(models.Model):
    name = models.CharField(max_length=100)
    credentials = models.TextField()
    achievements = models.TextField(null=True)
    experience = models.PositiveIntegerField(default=0, help_text="Number of years", null=True)
    specialities = models.ManyToManyField(Specialization)

    #Manager
    objects = models.Manager()
    prac_objects = PractitionerManager()
    
    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Cities"


class ClinicLocationManager(models.Manager):
    
    def clinic_detail(self, clinic_name):
        clininc_detail = super(ClinicLocationManager, self).filter(name=clinic_name).distinct()
        return clininc_detail

    def clinic_speciality(self, speciality, day):
        clininc_list = self.filter(practitioners__specialities__name=speciality,cliniclocationtiming__day=day).distinct()
        return clininc_list


class ClinicLocation(models.Model):
    practitioners = models.ManyToManyField(Practitioner)
    name = models.CharField(max_length=100,null=True)
    clinic_address = models.TextField()
    city = models.ForeignKey(City)
    contact_number = models.CharField(max_length=100)
    checkup_fee = models.PositiveIntegerField()
    services_offered = models.TextField(null=True, blank=True)
    appointments_only = models.BooleanField(default=True)
    lat = models.FloatField()
    lon = models.FloatField()
    # gis
    geo_objects = models.GeoManager()
    #Custom Managers
    objects = models.Manager()
    cl_objects = ClinicLocationManager()
    
    def __unicode__(self):
        return self.name


class ClinicLocationTimingManager(models.Manager):
    def clininc_day(self,day):
        return super(ClinicLocationTimingManager, self).filter(day=day)


class ClinicLocationTiming(models.Model):
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
    clinic_location = models.ForeignKey(ClinicLocation)
    day = models.CharField(max_length=3, choices=DAY, help_text="Select Day.")
    start_time = models.CharField(max_length=5, choices=TIME, help_text="Select starting Time for Clininc.")
    end_time = models.CharField(max_length=5, choices=TIME, help_text="Select ending Time for Clininc.")

    #Custom Managers
    objects = models.Manager()
    ct_objects = ClinicLocationTimingManager()