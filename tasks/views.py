import rest_framework
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


class TaskDeleteAPI(APIView):
    """
    Task delete API.
    """

    def delete(self, *args, **kwargs):
        task_id = self.request.query_params.get("task_id")
        instance = Task.objects.filter(id=task_id)
        if instance.exists():
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
