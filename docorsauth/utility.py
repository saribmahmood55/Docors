from .tasks import *


def send_activiation_link(user):
	"""
	The activation key for the ``docorsUser`` will be a
	SHA1 hash, generated from a combination of the user's
	email and a random salt.

	"""
	salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
	email = user.email
	if isinstance(email, unicode):
		email = email.encode('utf-8')
	activation_key = hashlib.sha1(salt+email).hexdigest()

	send_email(user, activation_key)