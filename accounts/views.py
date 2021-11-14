from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from accounts.serializers import RegisterSerializer, LoginSerializer


class RegisterAPI(APIView):
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            return Response(
                {"token": str(user.auth_token)}, status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    """
    User login.
    """

    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            token = serializer.validated_data
            return Response({"token": token}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAPI(APIView):
    """
    User logout.
    """

    def delete(self, *args, **kwargs):
        user = self.request.user
        token = Token.objects.get(user=user)
        if token:
            token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)