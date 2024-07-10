import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from server.apps.services import CustomModelViewSet, IsCreatorOrStaffPermission
from server.apps.surveys.api.serializers import OptionSerializer
from server.apps.surveys.models import Option


class OptionFilter(django_filters.FilterSet):
    """Фильтр для ответов"""

    class Meta:
        model = Option
        fields = {
            "is_correct": ["exact"],
        }


class OptionViewSet(CustomModelViewSet):
    """ViewSet для ответов"""

    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    search_fields = ["name"]
    ordering_fields = "__all__"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["question"]
    filterset_class = OptionFilter
    permission_classes = [IsCreatorOrStaffPermission, IsAuthenticated]
