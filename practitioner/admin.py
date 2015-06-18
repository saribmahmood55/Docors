from django.contrib import admin
from practitioner.models import *
from practice.models import *

class PracticeInline(admin.TabularInline):
	model = Practice
	extra = 1

class PractitionerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Title', {'fields': ['title']}),
		('Name', {'fields': ['name']}),
		('status', {'fields': ['status']}),
        ('Achievements', {'fields': ['achievements']}),
        ('Experience', {'fields': ['experience']}),
        ('Year of Birth', {'fields': ['year_of_birth']}),
        ('Gender', {'fields': ['gender']}),
        ('Thumbnail Photo ', {'fields': ['photo']}),
        ('Short Message', {'fields': ['message']}),
        ('Speciality', {'fields': ['specialities']}),
        ('Degrees', {'fields': ['degrees']}),
        ('Conditions', {'fields': ['conditions']}),
        ('Procedures', {'fields': ['procedures']}),
	]
	list_display = ['name','title','gender','Degrees_list','year_of_birth','experience','Specialist_in','Condtions_Treated','Procedures_Performed','pk']
	search_fields = ['name']
	inlines = [PracticeInline]
	
	def Specialist_in(self, obj):
		return " , ".join([s.name for s in obj.specialities.all()])

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
	list_filter = ['name']
	search_fields = ['name']

class ProcedureAdmin(admin.ModelAdmin):
	list_display = ['name','specialization','slug']
	list_filter = ['name']
	search_fields = ['name']


admin.site.register(Practitioner, PractitionerAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Procedure, ProcedureAdmin)