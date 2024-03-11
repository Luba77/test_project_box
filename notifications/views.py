from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .signals import send_notification_to_users


class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class UserNotificationsListView(generics.ListAPIView):
    serializer_class = UserNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserNotification.objects.filter(user=user)


class CreateNotification(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_notification_to_users(instance)


