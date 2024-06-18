from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from manager.models import Worker, Position


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="Admin",
            password="admin1234"
        )
        self.client.force_login(self.admin_user)

    def test_worker_position_displayed_in_list(self):
        position = Position.objects.create(name="Position")
        worker = Worker.objects.create(username="user", position=position)
        url = reverse("admin:manager_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, worker.position)

    def test_worker_position_displayed_in_detail(self):
        position = Position.objects.create(name="Position")
        worker = Worker.objects.create(username="user", position=position)
        url = reverse("admin:manager_worker_change", args=[worker.id])
        res = self.client.get(url)
        self.assertContains(res, worker.position)
