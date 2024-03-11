from django.urls import path
from .views import *


urlpatterns = [
    path('user-notifications/', UserNotificationsListView.as_view(), name='user-notifications'),
    path('all-notifications/', NotificationListView.as_view(), name='notification-list'),

]