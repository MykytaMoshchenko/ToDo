from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from to_do.forms import TaskCreateForm
from to_do.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    template_name = "to_do/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("to_do:index")
    form_class = TaskCreateForm


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("to_do:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("to_do:tag-list")


class UpdateStatusTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.is_completed:
            task.is_completed = False
        else:
            task.is_completed = True
        task.save()
        return redirect('to_do:index')


