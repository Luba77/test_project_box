from rest_framework import status, generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import ConfirmCode, User
from .serializers import UserCreateSerializer, UserAuthSerializer, UserCodeSerializer, UserDetailSerializer


class RegistrationCreateApiView(generics.CreateAPIView):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = UserCreateSerializer

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data='We send code on your email, go to link in message and enter code. '
                                 'If the message didn`t arrive, check if you wrote your email correctly')
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmCreateApiView(generics.CreateAPIView):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = UserCodeSerializer

    def post(self, request, *args, **kwargs):
        verification_code = request.data.get('verification_code')
        try:
            confirm_code = ConfirmCode.objects.get(verification_code=verification_code)
            if confirm_code.is_expired():
                return Response(data={"error": "Confirmation code has expired. Please register again."}, status=status.HTTP_400_BAD_REQUEST)
            user = confirm_code.user
            user.is_active = True
            user.save()
            return Response(data={"message": "User successfully confirmed."}, status=status.HTTP_200_OK)
        except ConfirmCode.DoesNotExist:
            return Response(data={"error": "Invalid confirmation code."}, status=status.HTTP_400_BAD_REQUEST)


class AuthorizationCreateApiView(generics.CreateAPIView):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = UserAuthSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'pk'
