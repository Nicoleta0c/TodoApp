from django.shortcuts import render
from rest_framework import viewsets

from todos.models import Task
from todos.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
