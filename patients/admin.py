from django.contrib import admin
from django.contrib.auth.models import User
from practitioner.models import Practitioner, Specialization
from patients.models import Patient


class PatientAdmin(admin.ModelAdmin):
	#inlines = (PatientInline, )
	list_display = ['patient_name','patient_user_name','email','cell_number','gender','age_group','Interested_Specialities','Favourite_Practitioners']

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

admin.site.register(Patient, PatientAdmin)