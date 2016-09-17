# flake8: noqa
from django.contrib import admin
from practitioner.models import *
from practice.models import *

class PracticeInline(admin.TabularInline):
	model = Practice
	extra = 1

class PractitionerAdmin(admin.ModelAdmin):
	{
	'fields': (('full_name', 'gender', 'email'), 'physician_type', 'degrees', 'year_of_birth',
		'specialty', 'fellowship', 'conditions', 'procedures'),
	}

	list_display = ['full_name', 'is_active', 'slug','gender','Degrees_list','specialty','Fellowship_in','Condtions_Treated','Procedures_Performed']
	search_fields = ['full_name']
	list_filter = ['full_name']
	inlines = [PracticeInline]

	def Fellowship_in(self, obj):
		return " , ".join([s.name for s in obj.fellowship.all()])

	def Degrees_list(self, obj):
		return " , ".join([d.name for d in obj.degrees.all()])

	def Condtions_Treated(self, obj):
		return " , ".join([d.name for d in obj.conditions.all()])

	def Procedures_Performed(self, obj):
		return " , ".join([d.name for d in obj.procedures.all()])

class SpecializationAdmin(admin.ModelAdmin):
	list_display = ['name','training_region','human_name','SEO_name', 'description', 'slug']
	list_filter = ['name']
	search_fields = ['name']

class DegreeAdmin(admin.ModelAdmin):
	list_display = ['name','points','color_code','description']
	list_filter = ['name']
	search_fields = ['name']

class ConditionAdmin(admin.ModelAdmin):
	list_display = ['name','specialization', 'fellowship', 'slug']
	list_filter = ['specialization']
	search_fields = ['name']

class ProcedureAdmin(admin.ModelAdmin):
	list_display = ['name', 'specialization', 'fellowship', 'slug']
	list_filter = ['specialization']
	search_fields = ['name']


class FellowshipAdmin(admin.ModelAdmin):
	list_display = ['name','specialization', 'description', 'slug']
	list_filter = ['specialization']
	search_fields = ['name']

class ClaimAdmin(admin.ModelAdmin):
	list_display = ['practitioner','email','pmdc_no','photo','current_status']
	list_filter = ['practitioner']
	search_fields = ['practitioner']

class UpdateInfoAdmin(admin.ModelAdmin):
	list_display = ['practitioner','ip','incorrect_info','correct_info','approved']
	list_filter = ['practitioner']
	search_fields = ['practitioner']


admin.site.register(Practitioner, PractitionerAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Fellowship, FellowshipAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(UpdateInfo, UpdateInfoAdmin)
