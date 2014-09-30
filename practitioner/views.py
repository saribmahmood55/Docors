from practitioner.models import Practitioner, ClinicLocation, ClinicLocationTiming

def practitioner_speciality(speciality):
	return Practitioner.objects.filter(specialities__name__icontains=speciality)

def practitioner_name(name):
	return Practitioner.objects.filter(name__icontains=name)

def practitioner_experience(name,experience):
	return Practitioner.objects.filter(name__icontains=name,experience__gte=experience)	


def practitioner_day(day,speciality):
	prac_list_speciality = ClinicLocation.objects.filter(practitioners__specialities__name__icontains=speciality)
	prac_list_day = ClinicLocationTiming.objects.filter(day__icontains=day,)
'''
def practitioner_day(day,number):
	Practitioner.objects.filter(specialities__name__icontains=name)
	clininc_list = ClinicLocationTiming.objects.filter(day__icontains=day)
	prac_list = []
	for one_clinic in clininc_list:
		prac_list += one_clinic.clinic_location.practitioners.filter(specialities__name=number)
		#exclude duplicates
		prac_list = list(set(prac_list))
	return prac_list
'''
#test queries sample
'''
from practitioner.views import *
doc = practitioner_speciality('child')
print doc[0].name
---
from practitioner.views import *
doc = practitioner_experience('anwar',20)
print doc[0].name
---
from practitioner.views import *
doc = practitioner_name('anwar')
print doc[0].name
---
'''