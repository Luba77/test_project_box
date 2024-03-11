from django.db import models

from main import settings



class Box(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    attempts = models.IntegerField()
    distribution_type = models.CharField(max_length=20, choices=[('random', 'Random'), ('uniform', 'Uniform')])
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_attempts = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    class Meta:
        db_table = 'boxes'


class UserBox(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    class Meta:
        db_table = 'user_boxes'
