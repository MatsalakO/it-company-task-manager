from django.test import TestCase
from django.utils import timezone

from manager.models import Position, TaskType, Worker, Task


class ModelTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create(
            username="User",
            position=self.position
        )
        self.task_type = TaskType.objects.create(name="Fix Smth")
        self.task = Task.objects.create(
            name="Fix critical bug",
            description="Fix a critical bug in the system",
            deadline=timezone.now().date() + timezone.timedelta(days=7),
            priority="Hi",
            task_type=self.task_type
        )
        self.task.assignees.add(self.worker)

    def test_task_type_str(self):
        task_type = TaskType.objects.get(name="Fix Smth")
        self.assertEqual(str(task_type), "Fix Smth")

    def test_position_str(self):
        position = Position.objects.get(name="Developer")
        self.assertEqual(str(position), "Developer")

    def test_task_str(self):
        expected_str = f"{self.task.name} with {self.task.priority} priority"
        self.assertEqual(str(self.task), expected_str)

    def test_task_clean_method_deadline(self):
        self.task.deadline = timezone.now().date() + timezone.timedelta(days=5)
        self.task.clean()
