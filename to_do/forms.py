from django import forms
from to_do.models import Task


class TaskCreateForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateTimeInput)

    class Meta:
        model = Task
        fields = "__all__"
