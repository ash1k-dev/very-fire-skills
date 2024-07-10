import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from server.apps.services import CustomModelViewSet
from server.apps.services.permissions import IsCreatorOrStaffPermission
from server.apps.surveys.api.serializers import SurveySerializer
from server.apps.surveys.models import Survey


class SurveyFilter(django_filters.FilterSet):
    """Фильтр для теста"""

    class Meta:
        model = Survey
        fields = {
            "title": ["exact", "icontains"],
            "description": ["exact", "icontains"],
        }


class SurveyViewSet(CustomModelViewSet):
    """ViewSet для тестов"""

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    search_fields = ["name"]
    ordering_fields = "__all__"
    filter_backends = [DjangoFilterBackend]
    filter_class = SurveyFilter
    permission_classes = [IsCreatorOrStaffPermission, IsAuthenticated]
