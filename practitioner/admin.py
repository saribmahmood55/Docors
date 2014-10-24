from django.contrib import admin
from practitioner.models import *


class PractitionerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Doctor/Practitioner Name', {'fields': ['name']}),
        ('Degrees/Credentials', {'fields': ['credentials']}),
        ('Achievements', {'fields': ['achievements']}),
        ('Experience', {'fields': ['experience']}),
        ('Short Message', {'fields': ['message']}),
        ('Speciality', {'fields': ['specialities']}),
	]
	list_display = ['name','slug','credentials','Specialist_in','experience','message','achievements']
	search_fields = ['name']
	
	def Specialist_in(self, obj):
		return "\n".join([s.name for s in obj.specialities.all()])


class PractiseLocationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Enter Name', {'fields': ['name']}),
		('Enter Address', {'fields': ['clinic_address']}),
		('Select City', {'fields': ['city']}),
        ('Enter Physical latitude', {'fields': ['lat']}),
        ('Enter Physical latitude', {'fields': ['lon']}),
	]
	list_display = ['name','slug','clinic_address','lat','lon']
	search_fields = ['name']


class PractiseAdmin(admin.ModelAdmin):
	fieldsets = [
		('Select Practise Location', {'fields': ['practise_location']}),
		('Select Practitioner', {'fields': ['practitioner']}),
        ('Enter Appointment Numbers', {'fields': ['contact_number']}),
        ('Enter Checkup Fees', {'fields': ['checkup_fee']}),
        ('Services Offered', {'fields': ['services']}),
        ('Appointments Only: Yes/No', {'fields': ['appointments_only']}),
	]
	list_display = ['practise_location','practitioner','contact_number','checkup_fee','services','appointments_only']
	search_fields = ['practitioner']


class PractiseTimingAdmin(admin.ModelAdmin):
	list_display = ['practitioner','practise_location','day', 'start_time','end_time']
	list_filter = ['day']
	search_fields = ['day']


class SpecializationAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	list_filter = ['name']
	search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	list_filter = ['name']
	search_fields = ['name']


admin.site.register(Practitioner, PractitionerAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(PractiseLocation, PractiseLocationAdmin)
admin.site.register(Practise, PractiseAdmin)
admin.site.register(PractiseTiming, PractiseTimingAdmin)
admin.site.register(Specialization, SpecializationAdmin)