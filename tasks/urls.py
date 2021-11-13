from django.urls import path

from tasks.views import TaskCreateAPI, TaskDeleteAPI

urlpatterns = [
    path("upload/", TaskCreateAPI.as_view(), name="create_new_task"),
    path("delete-task/", TaskDeleteAPI.as_view(), name="delete_task"),
]
