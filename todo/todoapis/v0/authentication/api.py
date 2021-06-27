from django.contrib.auth import get_user_model, authenticate

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_auth.models import TokenModel

from .serializer import LoginSerializer, RegisterSerializer


class LoginAPIView(generics.GenericAPIView):

    """
    Login API Admin/Contractor

    * Method : **POST**
    * Token : **No token required**
    * **Parameters**
        {
        &nbsp;&nbsp;&nbsp;&nbsp; "username": "char",
        &nbsp;&nbsp;&nbsp;&nbsp; "password": "char",
        }
    * **Parameters Example**
        {
        &nbsp;&nbsp;&nbsp;&nbsp; "username": "admin@email.com",
        &nbsp;&nbsp;&nbsp;&nbsp; "password": "Admin@123",
        }
    * **Response**
        {
        &nbsp;&nbsp;&nbsp;&nbsp; 'key': 'auth_token'
        }
    * **Response Example**
        {
        &nbsp;&nbsp;&nbsp;&nbsp; 'key': '49211b9fac668a3ee8e8e9876a4aabf3940efd23'
        }
    """

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        data = request.data
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid user details.'}, status=status.HTTP_403_FORBIDDEN)

        token, _ = TokenModel.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)


class RegisterAPIView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):

        data = request.data
        serializer = self.serializer_class(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        instance = serializer.save()
        instance.is_active = True
        instance.save()

        return Response({'message': 'Register successfully.'}, status=status.HTTP_200_OK)
