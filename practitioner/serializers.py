from django.forms import widgets
from rest_framework import serializers
from practitioner.models import *

class PractitionerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Practitioner
		fields = ('title','name','gender','year_of_birth','photo','email','experience','physician_type','achievements','message','degrees','specialities','slug','status','education_marks','recommendation','not_recommended','modified')

class SpecializationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Specialization
		fields = ('id','name','human_name','SEO_name','slug')

class DegreeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Degree
		fields = ('id','name','points','color_code','description')