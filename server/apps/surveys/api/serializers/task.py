from rest_framework import serializers
from server.apps.surveys.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer для модели тестового задания"""
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'survey',
            'created',
            'updated'
        )
        read_only_fields = (
            'id',
            'created',
            'updated'
        )
