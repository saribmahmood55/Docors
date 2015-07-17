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

	list_display = ['full_name','slug','gender','Degrees_list','specialty','Fellowship_in','Condtions_Treated','Procedures_Performed']
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
	list_display = ['name','human_name','SEO_name','slug']
	list_filter = ['name']
	search_fields = ['name']

class DegreeAdmin(admin.ModelAdmin):
	list_display = ['name','points','color_code','description']
	list_filter = ['name']
	search_fields = ['name']

class ConditionAdmin(admin.ModelAdmin):
	list_display = ['name','specialization','slug']
	list_filter = ['specialization']
	search_fields = ['name']

class ProcedureAdmin(admin.ModelAdmin):
	list_display = ['name','specialization','slug']
	list_filter = ['specialization']
	search_fields = ['name']


class FellowshipAdmin(admin.ModelAdmin):
	list_display = ['name','specialization','slug']
	list_filter = ['specialization']
	search_fields = ['name']


admin.site.register(Practitioner, PractitionerAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Procedure, ProcedureAdmin)
admin.site.register(Fellowship, FellowshipAdmin)