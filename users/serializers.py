from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from users.models import ConfirmCode
from django.core.mail import send_mail

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("telegram_id", "name", "date_joined",
                  "telegram_username", "name", "phone_number", "email", "language", "country")


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists! Choose other username.')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        confirm_code = ConfirmCode.objects.create(user=user)
        confirm_code.generate()
        confirm_code.save()
        try:
           send_mail(subject='Code for confirm of user',
                      message=f'Use this code ({confirm_code})',
                      from_email='testmail@gmail.com',
                      recipient_list=[user.email])
        except Exception as e:
            print(e)
            User.objects.get(username=user.username).delete()
            raise ValidationError('Code does not sent')
        return user


class UserCodeSerializer(serializers.Serializer):
    verification_code = serializers.CharField()


class UserProfileUpdateSerializer(serializers.Serializer):
    telegram_id = serializers.CharField()
    telegram_username = serializers.CharField()
    name = serializers.CharField()
    phone_number = serializers.CharField()
    language = serializers.CharField()
    country = serializers.CharField()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

