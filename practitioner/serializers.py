from django.forms import widgets
from rest_framework import serializers
from practitioner.models import Practitioner

class PractitionerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Practitioner
		fields = ('title','name','gender','year_of_birth','photo','email','experience','physician_type','achievements','message','degrees','specialities','slug','status','education_marks','recommendation','not_recommended','modified')