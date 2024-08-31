from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=255, unique=True, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

