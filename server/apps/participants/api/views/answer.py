from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from server.apps.participants.api.serializers.answer import AnswerSerializer
from server.apps.participants.models import Answer, ParticipantSurvey
from server.apps.surveys.models import Question, Option


class AnswerViewSet(viewsets.ModelViewSet):
    """ViewSet для ответов"""
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()



