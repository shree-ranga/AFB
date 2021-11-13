from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from tasks.serializers import Task, TaskSerializer


class TaskCreateAPI(APIView):
    """
    Task create API.
    """

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskUpdateDeleteAPI(APIView):
    """
    task update and delete API.
    """

    def get_object(self):
        task_id = self.kwargs["id"]
        obj = get_object_or_404(Task, pk=task_id)
        return obj

    # def put(self, *args, **kwargs):
    #     data = self.request.data
    #     instance = self.get_object()
    #     print(instance, data)
    #     serializer = TaskSerializer(instance, data=data)
    #     if serializer.is_valid():
    #         serializer.save(user=self.request.user)
    #         return Response(status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, *args, **kwargs):
        data = self.request.data
        instance = self.get_object()
        serializer = TaskSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, *args, **kwargs):
        task_id = kwargs["id"]
        instance = Task.objects.filter(id=task_id)
        if instance.exists():
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)