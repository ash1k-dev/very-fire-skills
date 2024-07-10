from rest_framework import serializers

from server.apps.surveys.api.serializers.option import (
    OptionParticipantSerializer,
    OptionSerializer,
)
from server.apps.surveys.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели вопроса"""
    class Meta:
        model = Question
        fields = (
            'id',
            'text',
            'survey',
            'question_weight',
            'created',
            'updated',
        )
        read_only_fields = (
            'id',
            'created',
            'updated',
        )



class QuestionParticipantSerializer(serializers.ModelSerializer):
    """Serializer для списка вопросов"""
    options = OptionParticipantSerializer(many=True)
    class Meta:
        model = Question
        fields = (
            'id',
            'text',
            'survey',
            'options',
        )
        read_only_fields = (
            'id',
        )
