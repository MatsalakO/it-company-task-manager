from django.urls import path

from manager.views import (
    index,
    TaskTypeListView,
    WorkerListView,
    TaskDetailView,
    TaskListView,
    WorkerDetailView,
    PositionListView,
    TaskTypeCreateView
)

app_name = "manager"

urlpatterns = [
    path("", index, name="index"),
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list"
    ),
    path(
        "task-types/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create"
    ),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
]
