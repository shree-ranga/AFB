from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status

from accounts.serializers import UserSerializer


class Register(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
