#flake8: noqa
import datetime
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from .managers import EmailConfirmationManager

# Here the magic happens enjoy.
# Custom User model

class docorsUserManager(BaseUserManager):
	def create_user(self, email, full_name, password=None):
		if not email:
			raise ValueError("User must provide an email address")

		user = self.model(email=self.normalize_email(email),full_name=full_name)
		if password:
			user.set_password(password)
		else:
			user.set_unusable_password()
		user.save(using=self._db)
		return user

	def create_superuser(self, email, full_name, password):
		user = self.create_user(email, password=password, full_name=full_name)
		user.is_admin = True
		user.is_active = True
		user.save(using=self._db)
		return user

class docorsUser(AbstractBaseUser):
	# this will be the identifier for the user model
	GENDER_CHOICES = ( ('M', 'Male'),('F', 'Female'), ('', 'Prefer not to disclose'))
	YEAR_CHOICES = []
	for r in range(1930, (datetime.datetime.now().year-12)):
		YEAR_CHOICES.append((r,r))
	
	email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
	full_name = models.CharField(max_length=100)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='', blank=True)
	year_of_birth = models.PositiveSmallIntegerField(
		'Year of Birth',
		choices=YEAR_CHOICES,
		default=1930,
		blank=True
	)

	modified = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	objects = docorsUserManager()
	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["full_name"]

	class Meta:
		verbose_name_plural = "Registered Users"

	def __str__(self):
		return self.full_name

	def get_full_name(self):
		return self.full_name

	def get_short_name(self):
		return self.email

	def has_perm(self, perm, obj=None):
		#THis will always return True
		return True

	def has_module_perms(self, app_label):
		#Check if the user has permission to a specific app mentioned by app_label
		#This will in most cases return True
		return True

	def email_user(self, subject, message, from_email=None, **kwargs):
		"""Send email to the user"""
		send_mail(subject,message,from_email,[self.email], **kwargs)

	@property
	def is_staff(self):
		#Check if the user is member of staff.
		#The simple answer is if the user is admin then yes
		return self.is_admin

class EmailConfirmation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_('user'))
    email = models.EmailField(unique=True,max_length=254,verbose_name=_('e-mail address'))
    created = models.DateTimeField(verbose_name=_('created'),default=timezone.now)
    sent = models.DateTimeField(verbose_name=_('sent'), null=True)
    key = models.CharField(verbose_name=_('key'), max_length=64, unique=True)
    verified = models.BooleanField(verbose_name=_('verified'), default=False)

    objects = EmailConfirmationManager()

    class Meta:
        verbose_name = _("email confirmation")
        verbose_name_plural = _("email confirmations")

    def __str__(self):
        return "confirmation for %s" % self.user

    @classmethod
    def create(cls, user):
        key = get_random_string(64).lower()
        return cls._default_manager.create(user=user, email=user.email, key=key)

    def key_expired(self):
        expiration_date = self.sent + datetime.timedelta(days=7)
        return expiration_date <= timezone.now()
    key_expired.boolean = True

    def email_sent(self):
    	self.sent = timezone.now()
    	self.save()
    	return self.sent

    def confirm_activation(self):
    	data = dict()
        if not self.key_expired() and not self.user.is_active:
            user = self.user
            user.is_active = True
            user.save()
            self.verified = True
            self.save()
            data['success'] = True
        elif self.key_expired:
        	data['success'] = False
        	data['error_message'] = 'Activation Key Expired'
        elif self.user.is_active:
        	data['success'] = False
        	data['error_message'] = 'Email address already verified'
        return data