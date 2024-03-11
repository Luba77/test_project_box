from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class UserBalanceDetailView(ListAPIView):
    serializer_class = UserBalanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserBalance.objects.filter(user=user)


class OperationsDetailView(ListAPIView):
    serializer_class = OperationsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Operation.objects.filter(user=user)


class CoinDetailView(RetrieveAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
