from django.contrib import admin
from practice.models import *

class CityAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	list_filter = ['name']
	search_fields = ['name']


class PracticeLocationAdmin(admin.ModelAdmin):
	list_display = ['pk','name','slug','clinic_address','lon','lat']
	search_fields = ['name']


class PracticeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['practitioner']}),
		(None, {'fields': ['practice_location']}),
		(None, {'fields': ['practice_type']}),
		(None, {'fields': ['practice_photo']}),
        (None, {'fields': ['contact_number']}),
        (None, {'fields': ['checkup_fee']}),
        (None, {'fields': ['services']}),
        (None, {'fields': ['appointments_only']}),
	]
	list_display = ['practitioner','pk','practice_location','contact_number','checkup_fee','appointments_only','modified','location']
	search_fields = ['practitioner__name']


class PracticeTimingAdmin(admin.ModelAdmin):
	list_display = ['practitioner','practice','day', 'start_time','end_time']
	list_filter = ['day']
	search_fields = ['practitioner__name','practice__practice_location__name','day']

class RecentSearchAdmin(admin.ModelAdmin):
	list_display = ['speciality','city','hit_count']


admin.site.register(City, CityAdmin)
admin.site.register(PracticeLocation, PracticeLocationAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(PracticeTiming, PracticeTimingAdmin)
admin.site.register(RecentSearch, RecentSearchAdmin)