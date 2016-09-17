from django.conf import settings
import requests

from practitioner.models import Practitioner

def get_client_ip(request):
    x_forwarded_for = request.META.get('X-Real-IP')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def validReCaptcha(request):
	parameters = {'secret': settings.RECAPTCHA_PRIVATE_KEY,'response': request.POST.get('g-recaptcha-response', ''), 'remoteip': get_client_ip(request) }
	r = requests.get("https://www.google.com/recaptcha/api/siteverify", params=parameters)
	response = r.json()
	return response['success']


def is_practitioner(user):
    try:
        pract = user.practitioner
        return True
    except Practitioner.DoesNotExist:
        return False
