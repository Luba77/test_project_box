from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class NotificationListView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class UserNotificationsListView(ListAPIView):
    serializer_class = UserNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserNotification.objects.filter(user=user)


