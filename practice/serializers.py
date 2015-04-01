from django.forms import widgets
from rest_framework import serializers
from practice.models import Practice

class PracticeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Practice
		fields = ('id','practice_type','practice_location','practitioner','fee','services','appointments_only','location')