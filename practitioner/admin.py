from django.contrib import admin
from practitioner.models import *


class PractitionerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Doctor/Practitioner Name', {'fields': ['name']}),
        ('Degrees/Credentials', {'fields': ['credentials']}),
        ('Achievements', {'fields': ['achievements']}),
        ('Experience', {'fields': ['experience']}),
        ('Speciality', {'fields': ['specialities']}),
	]
	list_display = ['name','slug','credentials','Specialist_in','experience','achievements']
	search_fields = ['name']
	
	def Specialist_in(self, obj):
		return "\n".join([s.name for s in obj.specialities.all()])


class ClinicLocationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Select Practitioner', {'fields': ['practitioners']}),
		('Enter Clinic/Hospital Name', {'fields': ['name']}),
        ('Clininc Street Address', {'fields': ['clinic_address']}),
        ('Select City', {'fields': ['city']}),
        ('Appointments Number', {'fields': ['contact_number']}),
        ('Checkup Fee', {'fields': ['checkup_fee']}),
        ('Services Offered', {'fields': ['services_offered']}),
        ('Appointments Only Yes/No', {'fields': ['appointments_only']}),
        ('Clininc Physical latitude', {'fields': ['lat']}),
        ('Clininc Physical latitude', {'fields': ['lon']}),
	]
	list_display = ['Practitioner_Clininc','name','clinic_address','services_offered','contact_number','checkup_fee','appointments_only','lat','lon']
	search_fields = ['name']


	def Practitioner_Clininc(self, obj):
		return "\n".join([s.name for s in obj.practitioners.all()])


class ClinicLocationTimingAdmin(admin.ModelAdmin):
	list_display = ['practitioner','clinic_location','day', 'start_time','end_time']
	list_filter = ['day']
	search_fields = ['day']


class SpecializationAdmin(admin.ModelAdmin):
	list_display = ['name']
	list_filter = ['name']
	search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
	list_display = ['name']
	list_filter = ['name']
	search_fields = ['name']


admin.site.register(Practitioner, PractitionerAdmin)
admin.site.register(ClinicLocationTiming, ClinicLocationTimingAdmin)
admin.site.register(ClinicLocation,ClinicLocationAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(City, CityAdmin)