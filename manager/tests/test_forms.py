from django.contrib.auth import get_user_model
from django.test import TestCase
from manager.forms import (
    PositionSearchForm,
    TaskTypeSearchForm,
    TaskSearchForm,
    WorkerSearchForm
)


class TaskFormsTests(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create_user(
            username="admin",
            password="password"
        )
        self.user2 = get_user_model().objects.create_user(
            username="admin2",
            password="password2"
        )

    def test_position_search_form_is_valid(self):
        form_data = {
            "name": "test",
        }
        form = PositionSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_task_type_search_form_is_valid(self):
        form_data = {
            "name": "Test",
        }
        form = TaskTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_task_search_form_is_valid(self):
        form_data = {
            "name": "Test",
        }
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_worker_search_form_is_valid(self):
        form_data = {
            "username": "user",
        }
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
