from django.shortcuts import render
from django.views import generic

from manager.models import Worker, Task, Position, TaskType


def index(request):
    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_positions = Position.objects.count()
    num_task_type = TaskType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
        "num_task_type": num_task_type,
        "num_visits": num_visits,
    }

    return render(request, "manager/index.html", context=context)


class TaskTypeListView(generic.ListView):
    model = TaskType
    queryset = TaskType.objects.order_by("name")
    paginate_by = 5


class PositionListView(generic.ListView):
    model = Position
    queryset = Position.objects.order_by("name")
    paginate_by = 5


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task


class WorkerListView(generic.ListView):
    model = Worker
    paginate_by = 5


class WorkerDetailView(generic.DetailView):
    model = Worker
    queryset = Worker.objects.prefetch_related("tasks__assignees")
