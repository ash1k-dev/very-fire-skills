import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from server.apps.companies.api.serializers import CompanySerializer
from server.apps.companies.models import Company
from server.apps.utils.views import CustomModelViewSet


class CompanyFilter(django_filters.FilterSet):
    """Фильтр для компании"""
    class Meta:
        model = Company
        fields = {
            "title": ["exact", "icontains"],
            'creator': ["exact"],
        }

class CompanyViewSet(CustomModelViewSet):
    """ViewSet для компании"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    search_fields = ["title"]
    ordering_fields = '__all__'
    filter_backends = [DjangoFilterBackend]
    filterset_class = CompanyFilter
    permission_classes = [IsAuthenticated]

