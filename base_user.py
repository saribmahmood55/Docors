# flake8: noqa
#  Tested built in functions
#  python manage.py shell
#  to update existing password
========================================================================
> python manage.py shell
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from students.models import WasheziUser
>>> from django.contrib.auth.hashers import check_password
>>> u = WasheziUser.objects.get(email='kashif@mailinator.com')
>>> u.set_password('abcd1234')
>>> u.save()
>>> p = u.password
>>> print check_password('abcd1234', p)
True
>>> print u.is_authenticated()
True
>>>
=========================================================================

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator


class BasicUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must provide an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class BasicUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    full_name = models.CharField(max_length=100)
    '''
    don't forget to exclude mobile number from base user model
    and include that in patient model :)
    '''
    mobile_number = models.BigIntegerField(
        db_index=True, unique=True,
        validators=[
            MaxValueValidator(
                3500000000,
                message="Please enter a valid mobile phone number e.g. "
                "03001234567"),
            MinValueValidator(
                3000000000,
                message="Please enter a valid mobile phone number e.g. "
                "03001234567")],
        help_text='Mobile phone number e.g. 03001234567'
    )
    modified = models.DateTimeField(auto_now=True)
    is_doctor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = BasicUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        verbose_name_plural = 'Registered Users'

    def __str__(self):
        return self.full_name

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_super_admin(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
