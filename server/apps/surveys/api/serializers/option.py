from rest_framework import serializers
from server.apps.surveys.models import Option


class OptionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели варианта ответа"""
    class Meta:
        model = Option
        fields = (
            'id',
            'text',
            'is_correct',
            'created',
            'updated',
        )
        read_only_fields = (
            'id',
            'created',
            'updated',
        )


class OptionParticipantSerializer(serializers.ModelSerializer):
    """Serializer для модели варианта ответа (для участников)"""
    class Meta:
        model = Option
        fields = (
            'id',
            'text',
        )
        read_only_fields = (
            'id',
        )
