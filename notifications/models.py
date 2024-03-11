from django.db import models
from main import settings


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()

    class Meta:
        db_table = 'notifications'

    def __str__(self):
        return f"Notification {self.id}"


class UserNotification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_notifications'

    def __str__(self):
        return f"{self.user} Notification {self.notification.id}"
