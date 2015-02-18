from django.contrib import admin
from practitioner.models import *
from practice.models import *

class PracticeTimingInline(admin.TabularInline):
	model = PracticeTiming
	extra = 1

class PractitionerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Title', {'fields': ['title']}),
		('Name', {'fields': ['name']}),
		('status', {'fields': ['status']}),
        ('Degrees/Credentials', {'fields': ['credentials']}),
        ('Achievements', {'fields': ['achievements']}),
        ('Experience', {'fields': ['experience']}),
        ('Short Message', {'fields': ['message']}),
        ('Speciality', {'fields': ['specialities']}),
	]
	list_display = ['name','title','slug','credentials','physician_type','Specialist_in','status','experience','modified','pk']
	search_fields = ['name']
	inlines = [PracticeTimingInline]
	
	def Specialist_in(self, obj):
		return "\n".join([s.name for s in obj.specialities.all()])

class SpecializationAdmin(admin.ModelAdmin):
	list_display = ['name','human_name','SEO_name','slug']
	list_filter = ['name']
	search_fields = ['name']

admin.site.register(Practitioner, PractitionerAdmin)
admin.site.register(Specialization, SpecializationAdmin)