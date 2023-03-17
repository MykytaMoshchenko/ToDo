from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField()
    tags = models.ManyToManyField(to=Tag, related_name="tasks")

    class Meta:
        ordering = ["is_completed", "deadline"]

    def __str__(self) -> str:
        return self.content
