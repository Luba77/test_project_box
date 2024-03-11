import random
from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django.conf import settings


class User(AbstractUser):
    telegram_id = models.CharField(max_length=100)
    telegram_username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True, max_length=100)
    language = models.CharField(max_length=100, choices=settings.LANGUAGES)
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')])
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'users'


class ConfirmCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.verification_code} {self.is_expired()}'

    class Meta:
        db_table = 'verification_code'
        verbose_name = 'Verification code'
        verbose_name_plural = 'Verifications codes'

    def generate(self):
        rand_code = ''
        for i in range(6):
            rand_code += str(random.randint(0, 9))
        self.verification_code = rand_code

    def is_expired(self):
        return timezone.now() - self.created_at > timedelta(hours=72)
