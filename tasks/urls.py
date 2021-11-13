from django.urls import path

from tasks.views import TaskCreateAPI, TaskUpdateDeleteAPI

urlpatterns = [
    path("upload/", TaskCreateAPI.as_view(), name="create_new_task"),
    path("task/<int:id>/", TaskUpdateDeleteAPI.as_view(), name="update_delete_task"),
]
