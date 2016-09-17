from django.forms import widgets
from rest_framework import serializers
from patients.models import Patient

class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ('id','user','cell_number','gender','age_group')