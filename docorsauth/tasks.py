from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email(user, activation_key):
	msg_plain = render_to_string('registration/activation_email.txt', {'user': user, 'activation_key': activation_key})
	msg_html = render_to_string('registration/email-template.html', {'user': user, 'activation_key': activation_key})

	d = Context({ 'user': user, 'activation_key': activation_key })

	send_mail('Welcome to Doctorsinfo. Pakistan | Account activation', msg_plain, 'no-reply@doctorsinfo.pk',[user.email, ],html_message=msg_html,)