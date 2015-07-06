from django.contrib import admin
from practitioner.models import Practitioner, Specialization
from patients.models import *

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ['email','cell_number','practitioner']
	search_fields = ['email']


class PatientAdmin(admin.ModelAdmin):
	list_display = ['patient_name','patient_user_name','email','cell_number','gender','age_group','city','Interested_Specialities','Favourite_Practitioners']
	search_fields = ['email']

	def patient_user_name(self, obj):
		return obj.user.username
	
	def patient_name(self, obj):
		return "%s %s" % (obj.user.first_name, obj.user.last_name)
	
	def email(self, obj):
		return obj.user.email

	def Interested_Specialities(self, obj):
		return "\n".join([specialities.name for specialities in obj.interested_specialities.all()])

	def Favourite_Practitioners(self, obj):
		return "\n".join([practitioner.name for practitioner in obj.favt_practitioner.all()])

admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Patient, PatientAdmin)
