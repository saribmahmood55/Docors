from django.core.mail import send_mail
from django.conf import settings
import requests

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
	print 'captcha', response['success']
	return response['success']


def confirmation_mail(practitioner):
	subject = "Registration Request | " + practitioner.name
	message = "Hi "+practitioner.name+",\n\nYour Practice information has been recieved successfully.\nYour Practice details will be public on http://www.doctorsinfo.pk in next 24-36 Hours.\nDoctors Info. Pakistan will never public your email address.\nIn order to make any changes in your Practice details(i.e Contact Number, Address, Check up fee or Timings) you can drop us an email with that email id and subject as: "+practitioner.slug+"\nKeep Serving Pakistan !\n\nRegards:\nDoctors Info. Pakistan."
	sender = 'doctorsinfo.pk@gmail.com'
	recepient = practitioner.email
	
	send_mail(subject, message, sender, [recepient], fail_silently=False)
	print "confirmation_mail"