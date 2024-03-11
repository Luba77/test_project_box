from django.urls import path
from .views import *


urlpatterns = [
    path('user-notifications/', UserNotificationsListView.as_view(), name='user-notifications'),
    path('all-notifications/', NotificationListView.as_view(), name='notification-list'),
    path('notifications/create/', CreateNotification.as_view(), name='create_notification'),

]