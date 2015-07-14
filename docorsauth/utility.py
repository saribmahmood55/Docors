from docorsauth.models import EmailConfirmation
from .tasks import *


def send_activation_link(user):
	"""
	The activation key for the ``docorsUser`` will be a
	SHA1 hash, generated from a combination of the user's
	email and a random salt.

	"""
	email_confirm = EmailConfirmation.create(user)
	
	send_email(email_confirm)