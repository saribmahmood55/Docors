# flake8: noqa
""" Custom Template processor to handle the user data sent to the template
and also add the city variable to the response object
written by Sarib """

from practice.models import City, Area
from patients.models import Patient

def customProcessor(request):
	sticky_data = {}
	sticky_data['user'] = request.user if request.user.is_authenticated() else None
	sticky_data['cities'] = City.objects.order_by('pk')
	sticky_data['user_city'] = City.city_objects.get_default()
	
	# try:
	# 	sticky_data['user_city'] = Patient.patient_objects.get_city(user=sticky_data['user'])
	# except Patient.DoesNotExist:
	# 	sticky_data['user_city'] = City.city_objects.get_default()

	sticky_data['areas'] = Area.area_objects.get_areas(city=sticky_data['user_city'])
	return {'sticky_data':sticky_data}