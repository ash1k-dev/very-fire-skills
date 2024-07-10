from rest_framework import viewsets

from server.apps.participants.api.serializers.answer import AnswerSerializer
from server.apps.participants.models import Answer


class AnswerViewSet(viewsets.ModelViewSet):
    """ViewSet для ответов"""

    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
