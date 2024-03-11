from django.urls import path
from .views import *

urlpatterns = [
    path('user-balance/', UserBalanceDetailView.as_view(), name='user-balance'),
    path('user-operation/', OperationsDetailView.as_view(), name='user-operation'),
    path('coins/<int:pk>/', CoinDetailView.as_view(), name='coin-detail'),
]