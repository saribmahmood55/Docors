from practitioner.models import *
from django.template import Library
register = Library()

@register.filter
def times(number):
    return range(number)
'''
@register.filter
def clinic_name(query):
	practise_location = []
	test = query[0].practise_location
	print test
	count = 0
	for one in query:
		if one.practise_location == test:
			practise_location[count] += one
		else:
			count += 1
			test = one.practise_location
	return practise_location
'''