from rest_framework import serializers

from server.apps.participants.models.relation import ParticipantSurvey
from server.apps.surveys.api.serializers import (
    OptionSerializer,
    QuestionSerializer,
)


class ParticipantSurveySerializer(serializers.ModelSerializer):
    """Serializer для связи участника и опроса"""
    class Meta:
        model = ParticipantSurvey
        fields = '__all__'

