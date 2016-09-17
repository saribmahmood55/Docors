from datetime import timedelta

from django.utils import timezone
from django.db import models
from django.db.models import Q
from django.conf import settings

class EmailConfirmationManager(models.Manager):

    def all_expired(self):
        return self.filter(self.expired_q())

    def all_valid(self):
        return self.exclude(self.expired_q())

    def expired_q(self):
        sent_threshold = timezone.now() - timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        return Q(sent__lt=sent_threshold)

    def delete_expired_confirmations(self):
        self.all_expired().delete()