from rest_framework import serializers
from .models import *


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'


class UserBoxSerializer(serializers.ModelSerializer):
    box = BoxSerializer()

    class Meta:
        model = UserBox
        fields = ['user', 'box', 'status']


class BoxUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['current_amount', 'current_attempts']
