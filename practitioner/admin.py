from django.contrib import admin
from practitioner.models import Practitioner, Specialization, ClinicLocation, ClinicLocationTiming, City


class PractitionerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Doctor/Practitioner Name', {'fields': ['name']}),
        ('Degrees/Credentials', {'fields': ['credentials'], 'classes': ['collapse']}),
        ('Achievements', {'fields': ['achievements'], 'classes': ['collapse']}),
        ('Experience', {'fields': ['experience'], 'classes': ['collapse']}),
        ('Speciality', {'fields': ['specialities'], 'classes': ['collapse']}),
	]
	#inlines = [ClinicLocationInline]
	list_display = ['name','credentials','Specialist_in','experience','achievements']
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
	list_display = ['clinic_location','day', 'start_time','end_time']
	list_filter = ['day']
	search_fields = ['day']
	extra = 3


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