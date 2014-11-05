from django.contrib import admin
from practice.models import *

class CityAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	list_filter = ['name']
	search_fields = ['name']


class PracticeLocationAdmin(admin.ModelAdmin):
	fieldsets = [
		('Enter Name', {'fields': ['name']}),
		('Enter Address', {'fields': ['clinic_address']}),
		('Select City', {'fields': ['city']}),
		('Enter Physical latitude', {'fields': ['lon']}),
        ('Enter Physical latitude', {'fields': ['lat']}),
	]
	list_display = ['name','slug','clinic_address','lat','lon']
	search_fields = ['name']


class PracticeAdmin(admin.ModelAdmin):
	fieldsets = [
		('Select Practitioner', {'fields': ['practitioner']}),
		('Select Practice Location', {'fields': ['practice_location']}),
		('Select Practice Type', {'fields': ['practice_type']}),
        ('Enter Appointment Numbers', {'fields': ['contact_number']}),
        ('Enter Checkup Fees', {'fields': ['checkup_fee']}),
        ('Services Offered', {'fields': ['services']}),
        ('Appointments Only: Yes/No', {'fields': ['appointments_only']}),
	]
	list_display = ['practice_location','practitioner','contact_number','checkup_fee','services','modified','appointments_only','location']
	search_fields = ['practitioner']


class PracticeTimingAdmin(admin.ModelAdmin):
	list_display = ['practitioner','practice','day', 'start_time','end_time']
	list_filter = ['day']
	search_fields = ['day']


admin.site.register(City, CityAdmin)
admin.site.register(PracticeLocation, PracticeLocationAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(PracticeTiming, PracticeTimingAdmin)