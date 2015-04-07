from django.forms import widgets
from rest_framework import serializers
from practice.models import *

class PracticeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Practice
		fields = ('id','practice_type','practice_location','practitioner','fee','services','appointments_only','location')

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ('id', 'name')

class CheckupFeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CheckupFee
		fields = ('id', 'amount')