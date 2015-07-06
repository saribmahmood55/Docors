from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator

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
		user.save(using=self._db)
		return user

class docorsUser(AbstractBaseUser):
	# this will be the identifier for the user model
	email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
	full_name = models.CharField(max_length=100)

	modified = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)
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

	@property
	def is_staff(self):
		#Check if the user is member of staff.
		#The simple answer is if the user is admin then yes
		return self.is_admin