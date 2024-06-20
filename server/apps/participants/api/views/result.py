from rest_framework import viewsets
from server.apps.participants.api.serializers.result import ResultSerializer
from server.apps.participants.models import Result


class ResultViewSet(viewsets.ModelViewSet):
    """ViewSet для результатов опроса"""
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
