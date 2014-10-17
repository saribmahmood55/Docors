from django.contrib import admin
from django.contrib.auth.models import User
from patients.models import Patient, PractitionerReview
from practitioner.models import Practitioner, Specialization


class PatientAdmin(admin.ModelAdmin):
	#inlines = (PatientInline, )
	list_display = ['patient_name','patient_user_name','email','cell_number','gender','Interested_Specialities','Favourite_Practitioners']

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


class PractitionerReviewAdmin(admin.ModelAdmin):
	list_display = ['practitioner','patient','post_as_anonymous','review_text','Practitioner_Reviewed','Reviewed_By','review_date','up_votes','down_votes']
	list_filter = ['review_date']

	def Practitioner_Reviewed(self, obj):
		return obj.practitioner.name

	def Reviewed_By(self, obj):
		return "%s %s" % (obj.patient.user.first_name, obj.patient.user.last_name)

#admin.site.unregister(User)
admin.site.register(Patient, PatientAdmin)
admin.site.register(PractitionerReview, PractitionerReviewAdmin)

#"\n".join([patient.name for patient in obj.patient.all()])
#"\n".join([practitioner.name for practitioner in obj.practitioners.all()])