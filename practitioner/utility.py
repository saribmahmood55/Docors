from django.core.mail import send_mail

def Email(practitioner, body):
	recepient = 'doctorsinfo.pk@gmail.com'
	subject = "Info. Update Request | " + practitioner
	email = ''
	#send email
	send_mail(subject, body, email, [recepient])
	print "Email sent"