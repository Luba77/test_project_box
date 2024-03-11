from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from users.models import User
from .models import Notification, UserNotification


@receiver(post_save, sender=Notification)
def send_notification_to_users(instance, **kwargs):
    users = User.objects.all()
    for user in users:
        UserNotification.objects.create(user=user, notification=instance)
        send_mail(
            'New Notification',
            instance.text,
            'your_email@example.com',
            [user.email],
            fail_silently=False,
        )

