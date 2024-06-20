import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from server.apps.surveys.api.serializers import TaskSerializer
from server.apps.surveys.models import Task
from server.apps.utils import CustomModelViewSet, IsCreatorOrStaffPermission


class TaskFilter(django_filters.FilterSet):
    """Фильтр для задач"""
    class Meta:
        model = Task
        fields = {
            'title': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],
        }

class TaskViewSet(CustomModelViewSet):
    """ViewSet для задач"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ["name"]
    ordering_fields = '__all__'
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter
    permission_classes = [IsCreatorOrStaffPermission, IsAuthenticated]



