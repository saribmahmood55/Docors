# flake8: noqa
from django.contrib import admin
from practice.models import *

class CityAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	list_filter = ['name']
	search_fields = ['name']

class AreaAdmin(admin.ModelAdmin):
	list_display = ['name', 'city', 'slug']
	list_filter = ['city']
	search_fields = ['name']

class CheckupFeeAdmin(admin.ModelAdmin):
	list_display = ['amount']
	list_filter = ['amount']


class PracticeLocationAdmin(admin.ModelAdmin):
	list_display = ['name','slug','area','contact_number','clinic_address','lon','lat']
	search_fields = ['name']


class PracticeAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['practitioner']}),
		(None, {'fields': ['practice_location']}),
		(None, {'fields': ['practice_type']}),
        (None, {'fields': ['fee']}),
        (None, {'fields': ['phone_ext']}),
        (None, {'fields': ['appointments_only']}),
	]
	list_display = ['practitioner','pk','practice_location','fee', 'phone_ext', 'appointments_only','modified']
	search_fields = ['practitioner__name']


class PracticeTimingAdmin(admin.ModelAdmin):
	list_display = ['practice','day', 'start_time','end_time']
	list_filter = ['day']
	search_fields = ['practice__practice_location__name','day']

class RecentSearchAdmin(admin.ModelAdmin):
	list_display = ['specialty','city','hit_count']


admin.site.register(City, CityAdmin)
admin.site.register(CheckupFee, CheckupFeeAdmin)
admin.site.register(PracticeLocation, PracticeLocationAdmin)
admin.site.register(Practice, PracticeAdmin)
admin.site.register(PracticeTiming, PracticeTimingAdmin)
admin.site.register(RecentSearch, RecentSearchAdmin)
admin.site.register(Area, AreaAdmin)