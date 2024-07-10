from rest_framework import serializers

from server.apps.companies.api.serializers.company import (
    CompanyParticipantSerializer,
)
from server.apps.surveys.models import Survey


class SurveySerializer(serializers.ModelSerializer):
    """Сериализатор для модели опроса"""
    class Meta:
        model = Survey
        fields = (
            'id',
            'title',
            'company',
            'time_limit',
            'passing_score',
            'description',
            'created',
            'updated',
        )
        read_only_fields = (
            'id',
            'created',
            'updated',
        )


class SurveyParticipantSerializer(serializers.ModelSerializer):
    """Serializer для модели опроса (для участников)"""
    company = CompanyParticipantSerializer(many=False, read_only=True)
    class Meta:
        model = Survey
        fields = (
            'id',
            'title',
            'time_limit',
            'description',
            'company',
        )
        read_only_fields = (
            'id',
        )
