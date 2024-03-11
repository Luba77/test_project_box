from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class BoxDetailView(generics.RetrieveAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    lookup_field = 'pk'


class UserBoxesListView(generics.ListAPIView):
    serializer_class = UserBoxSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserBox.objects.filter(user=user)


class BoxUpdateView(generics.UpdateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxUpdateSerializer
    lookup_url_kwarg = 'pk'

    def put(self, request, *args, **kwargs):
        box_id = kwargs.get(self.lookup_url_kwarg)
        try:
            box = Box.objects.get(pk=box_id)
        except Box.DoesNotExist:
            return Response({'error': 'Box not found'}, status=status.HTTP_404_NOT_FOUND)

        # Update the current amount and attempts
        current_amount = request.data.get('current_amount')
        current_attempts = request.data.get('current_attempts')

        if current_amount is not None:
            box.current_amount = current_amount
        if current_attempts is not None:
            box.current_attempts = current_attempts

        box.save()

        serializer = self.get_serializer(box)
        return Response(serializer.data)