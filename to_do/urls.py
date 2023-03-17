from django.urls import path

from to_do.views import (
    TaskListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    UpdateStatusTaskView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path('task/<int:pk>/status_update/', UpdateStatusTaskView.as_view(), name="update-status-task"),
]

app_name = "ToDo_list"
