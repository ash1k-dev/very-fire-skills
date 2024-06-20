import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from server.apps.surveys.api.serializers import QuestionSerializer
from server.apps.surveys.models import Question
from server.apps.utils import CustomModelViewSet, IsCreatorOrStaffPermission


class QuestionFilter(django_filters.FilterSet):
    """Фильтр для вопросов"""
    class Meta:
        model = Question
        fields = {
            'text': ['exact', 'icontains'],
            'question_weight': ['exact', 'icontains'],
        }

class QuestionViewSet(CustomModelViewSet):
    """ViewSet для вопросов"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    search_fields = ["name"]
    ordering_fields = '__all__'
    filter_backends = [DjangoFilterBackend]
    filterset_class = QuestionFilter
    permission_classes = [IsCreatorOrStaffPermission, IsAuthenticated]





