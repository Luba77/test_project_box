from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class UserBalanceDetailView(generics.ListAPIView):
    serializer_class = UserBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserBalance.objects.filter(user=user)


class OperationsDetailView(generics.ListAPIView):
    serializer_class = OperationsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Operation.objects.filter(user=user)


class CoinDetailView(generics.RetrieveAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
