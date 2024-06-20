from rest_framework.serializers import ModelSerializer
from server.apps.companies.models.company import Company


class CompanySerializer(ModelSerializer):
    """Serializer для модели компании"""
    class Meta:
        model = Company
        fields = (
            'id',
            'title',
            'description',
            'created',
            'updated',
        )
        read_only_fields = (
            'id',
            'created',
            'updated',
        )


class CompanyParticipantSerializer(ModelSerializer):
    """Serializer для компании"""
    class Meta:
        model = Company
        fields = (
            'title',
        )
        read_only_fields = (
            'id',
        )
