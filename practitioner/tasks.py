from __future__ import absolute_import
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def add(x, y):
	print x+y
	return x + y


@shared_task
def confirmation_mail(email_details):
	subject = "Registration Request | " + email_details['name']
	message = "Hi "+email_details['name']+",\n\nYour Practice information has been recieved successfully, It will be availabe to everyone on http://www.doctorsinfo.pk in next 24-36 Hours. Doctors Info. Pakistan will never public your email address.\nIn order to make any changes in your Practice details(i.e Contact Number, Address, Check up fee or Timings) you can drop us an email with that email id and subject as: "+email_details['slug']+"\n\nKeep Serving Pakistan !\n\nRegards:\nDoctors Info. Pakistan."
	sender = 'doctorsinfo.pk@gmail.com'
	recepient = email_details['email']
	if send_mail(subject, message, sender, [recepient], fail_silently=True):
		return True
	else:
		return False