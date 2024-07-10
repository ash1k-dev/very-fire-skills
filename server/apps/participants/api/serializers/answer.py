from rest_framework import serializers

from server.apps.participants.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Serializer для ответов"""
    class Meta:
        model = Answer
        fields = "__all__"
