from django.urls import path
from .views import *

urlpatterns = [
    path('user-boxes/', UserBoxesListView.as_view(), name='user-boxes'),
    path('boxes-detail/<int:pk>/', BoxDetailView.as_view(), name='box-detail'),
    path('boxes-open/<int:pk>/', BoxUpdateView.as_view(), name='box-open'),
]
