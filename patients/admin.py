from django.contrib import admin
from patients.models import Patient, PractitionerReview
from practitioner.models import Practitioner, Specialization


class PatientAdmin(admin.ModelAdmin):
	list_display = ['name','email','cell_number','gender','Interested_Specialities','Favourite_Practitioners']

	def Interested_Specialities(self, obj):
		return "\n".join([specialities.name for specialities in obj.interested_specialities.all()])

	def Favourite_Practitioners(self, obj):
		return "\n".join([practitioner.name for practitioner in obj.favt_practitioner.all()])


class PractitionerReviewAdmin(admin.ModelAdmin):
	list_display = ['review_text','Practitioner_Reviewed','Reviewed_By','review_date','up_votes','down_votes']
	list_filter = ['review_date']

	def Practitioner_Reviewed(self, obj):
		return "\n".join([practitioner.name for practitioner in obj.practitioner.all()])

	def Reviewed_By(self, obj):
		return "\n".join([patient.name for patient in obj.patient.all()])

admin.site.register(Patient, PatientAdmin)
admin.site.register(PractitionerReview,PractitionerReviewAdmin)
