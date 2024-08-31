from rest_framework import serializers

from todos.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "url", "description", "completed")
