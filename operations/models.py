import uuid
from django.db import models
from boxes.models import Box
from main import settings
from users.models import User


class Operation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('credited', 'Credited'), ('debited', 'Debited')])

    class Meta:
        db_table = 'operations'


class Coin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    class Meta:
        db_table = 'coins'

    def __str__(self):
        return self.name


class UserBalance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'balance'
        unique_together = ('user', 'coin',)
