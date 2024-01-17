from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.urls import reverse

from manager.models import TaskType, Position, Worker, Task


class TaskManagerViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username="User",
            password="password"
        )
        self.client.force_login(self.user)

    def test_index_view(self):
        response = self.client.get(reverse("manager:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/index.html")

    def test_task_type_list_view(self):
        TaskType.objects.create(name="Fix")
        TaskType.objects.create(name="Fix 2")
        response = self.client.get(reverse("manager:task-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/tasktype_list.html")

    def test_task_type_create_view(self):
        response = self.client.get(reverse("manager:task-type-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/tasktype_form.html")

    def test_task_type_update_view(self):
        task_type = TaskType.objects.create(name="Type 1")
        response = self.client.get(reverse(
            "manager:task-type-update",
            args=[task_type.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/tasktype_form.html")

    def test_task_type_delete_view(self):
        task_type = TaskType.objects.create(name="Type 1")
        response = self.client.get(reverse(
            "manager:task-type-delete",
            args=[task_type.pk]
        ))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "manager/tasktype_confirm_delete.html"
        )

    def test_task_list_view(self):
        task_type = TaskType.objects.create(name="Developing")
        Task.objects.create(
            name="Dev 1",
            description="Description",
            deadline="2024-12-31",
            is_completed=False,
            task_type=task_type
        )
        Task.objects.create(
            name="Dev 2",
            description="Description 2",
            deadline="2024-12-31",
            is_completed=True,
            task_type=task_type
        )
        response = self.client.get(reverse("manager:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/task_list.html")

    def test_worker_list_view(self):
        Position.objects.create(name="Tester")
        Worker.objects.create(
            username="Test",
            position=Position.objects.first()
        )
        Worker.objects.create(
            username="tester",
            position=Position.objects.first()
        )
        response = self.client.get(reverse("manager:worker-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "manager/worker_list.html")
