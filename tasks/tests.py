from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient

from tasks.models import Task

User = get_user_model()


class TestSetup(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user", password="strong-password"
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.create_task_url = reverse("create_new_task")
        self.create_task_data_no_due_date = {"title": "Testing create task."}
        self.fail_due_date = "2021-1-1"
        self.create_task_data_fail_due_date = {
            "title": "Testing create task.",
            "due_date": self.fail_due_date,
        }
        self.success_due_date = "2022-1-1"
        self.create_task_data_correct_due_date = {
            "title": "Testing create task.",
            "due_date": self.success_due_date,
        }

        self.task = Task.objects.create(title="update task test", user=self.user)
        self.update_delete_task_url = reverse(
            "update_delete_task", kwargs={"id": self.task.id}
        )
        self.update_task_data_success_due_date = {"due_date": self.success_due_date}
        self.update_task_data_fail_due_date = {"due_date": self.fail_due_date}
        self.update_task_title = {"title": "New test title"}

        self.list_user_task_url = reverse("user_tasks_list")
        self.list_user_task_priority_ordering_url = (
            "http://127.0.0.1:8000/tasks/list/?ordering=priority"
        )

        return super().setUp()


class TaskTests(TestSetup):
    def test_create_task_correct_data_no_due_date(self):
        res = self.client.post(
            self.create_task_url, self.create_task_data_no_due_date, format="json"
        )
        self.assertEqual(res.status_code, 201)

    def test_create_task_incorrect_due_date(self):
        res = self.client.post(
            self.create_task_url, self.create_task_data_fail_due_date, format="json"
        )
        self.assertEqual(res.status_code, 400)

    def test_create_task_correct_due_date(self):
        res = self.client.post(
            self.create_task_url, self.create_task_data_correct_due_date, format="json"
        )
        self.assertEqual(res.status_code, 201)

    def test_task_update_correct_due_date(self):
        res = self.client.patch(
            self.update_delete_task_url,
            self.update_task_data_success_due_date,
            format="json",
        )
        self.assertEqual(res.status_code, 201)

    def test_task_update_fail_due_date(self):
        res = self.client.patch(
            self.update_delete_task_url,
            self.update_task_data_fail_due_date,
            format="json",
        )
        self.assertEqual(res.status_code, 400)

    def test_task_update_title(self):
        res = self.client.patch(
            self.update_delete_task_url,
            self.update_task_title,
            format="json",
        )
        self.assertEqual(res.status_code, 201)

    def test_task_delete(self):
        res = self.client.delete(
            self.update_delete_task_url,
        )
        self.assertEqual(res.status_code, 204)

    def test_tasks_list(self):
        res = self.client.get(self.list_user_task_url)
        self.assertEqual(res.status_code, 200)

    def test_tasks_list_sorted_priority(self):
        res = self.client.get(self.list_user_task_priority_ordering_url)
        self.assertEqual(res.status_code, 200)
