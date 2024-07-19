from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")


class TaskToggleView(generic.View):
    @staticmethod
    def get(request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.done = not task.done
        task.save()
        return redirect("todo:task-list")
