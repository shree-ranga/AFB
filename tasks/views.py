from django.shortcuts import get_object_or_404

from django_filters import rest_framework as filters

from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

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


class UserTaskListAPI(generics.ListAPIView):
    """
    Fetches users task list.
    Is sortable based on priority.
    Also can be filtered based on task label and completion status.
    """

    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["label", "completed"]

    def get_queryset(self):
        user = self.request.user
        return user.tasks.all()


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
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
