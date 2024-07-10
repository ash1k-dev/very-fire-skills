from rest_framework import serializers

from server.apps.participants.models import Result


class ResultSerializer(serializers.ModelSerializer):
    """Serializer для результатов опросов"""
    class Meta:
        model = Result
        fields = "__all__"
