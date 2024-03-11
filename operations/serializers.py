from rest_framework import serializers
from .models import *


class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBalance
        fields = ['user', 'coin', 'balance']


class OperationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = '__all__'
