from django.urls import path

from tasks.views import TaskCreateAPI, TaskUpdateDeleteAPI, UserTaskListAPI

urlpatterns = [
    path("upload/", TaskCreateAPI.as_view(), name="create_new_task"),
    path("<int:id>/", TaskUpdateDeleteAPI.as_view(), name="update_delete_task"),
    path("list/", UserTaskListAPI.as_view(), name="user_tasks_list"),
]
