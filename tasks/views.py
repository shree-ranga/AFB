from django.shortcuts import get_object_or_404

from django_filters import rest_framework as filters

from rest_framework import generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.permissions import IsOwner
from tasks.serializers import Task, TaskSerializer


class TaskCreateAPI(APIView):
    """
    Task create API.
    """

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = TaskSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(status=status.HTTP_201_CREATED)


class UserTaskListAPI(generics.ListAPIView):
    """
    Fetches user's tasks list.
    Is sortable based on priority.
    Also can be filtered based on task label, priority, and completion status.
    """

    serializer_class = TaskSerializer
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter]
    filterset_fields = [
        "label",
        "priority",
        "completed",
    ]

    def get_queryset(self):
        user = self.request.user
        return user.tasks.all()


class TaskUpdateDeleteAPI(APIView):
    """
    Task update and delete API.
    """

    permission_classes = [IsOwner]

    def get_object(self):
        task_id = self.kwargs["id"]
        obj = get_object_or_404(Task, pk=task_id)
        return obj

    def patch(self, *args, **kwargs):
        data = self.request.data
        instance = self.get_object()
        serializer = TaskSerializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
