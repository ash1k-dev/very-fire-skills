import django_filters
from django.db.models import OuterRef, Prefetch, Subquery
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from server.apps.participants.api.serializers import AnswerSerializer
from server.apps.participants.api.serializers.relation import (
    ParticipantSurveySerializer,
)
from server.apps.participants.models import Answer, Result
from server.apps.participants.models.relation import ParticipantSurvey
from server.apps.services import CustomModelViewSet, IsCreatorOrStaffPermission
from server.apps.surveys.api.serializers import (
    OptionParticipantSerializer,
    QuestionSerializer,
)
from server.apps.surveys.api.serializers.question import (
    QuestionParticipantSerializer,
)
from server.apps.surveys.api.serializers.survey import (
    SurveyParticipantSerializer,
)
from server.apps.surveys.models import Question, Survey


class ParticipantSurveyFilter(django_filters.FilterSet):
    """Фильтр для задач"""

    class Meta:
        model = ParticipantSurvey
        fields = {
            "uuid": ["exact", "icontains"],
        }


class ParticipantSurveyViewSet(CustomModelViewSet):
    """ViewSet для связи участников и опросов"""

    queryset = ParticipantSurvey.objects.all()
    serializer_class = ParticipantSurveySerializer
    search_fields = ["title"]
    ordering_fields = "__all__"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["participant", "survey"]
    filterset_class = ParticipantSurveyFilter
    # permission_classes = [IsCreatorOrStaffPermission]

    @action(
        detail=True,
        url_path="start-survey",
        methods=["get"],
        serializer_class=SurveyParticipantSerializer,
        permission_classes=[AllowAny],
    )
    def start_survey(self, request, pk=None):
        """Получение информации об опросе для отображения перед стартом теста"""
        participant_survey = self.get_object()
        print("------------------------------------")
        print(pk)
        print("------------------------------------")
        try:
            related_object = participant_survey.results
            return Response(
                status=status.HTTP_400_BAD_REQUEST, data="Данный опрос уже был пройден"
            )
        except:
            serializer = self.get_serializer(participant_survey.survey)
            return Response(serializer.data)

    @action(
        detail=True,
        url_path="end-survey",
        methods=["get"],
        serializer_class=QuestionParticipantSerializer,
        permission_classes=[AllowAny],
    )
    def end_survey(self, request, *args, **kwargs):
        """Запись и отправка результатов опроса"""
        participant_survey = self.get_object()
        passing_score = participant_survey.survey.passing_score
        all_answers = participant_survey.answers.all().count()
        if all_answers == 0:
            Result.objects.create(participant_survey=participant_survey, result=0)
        else:
            correct_answers = (
                participant_survey.answers.all().filter(option__is_correct=True).count()
            )
            result_score = (correct_answers / all_answers) * 100
            if result_score >= passing_score:
                # здесь отправка задания через celery и/или уведомление менеджера
                if participant_survey.survey.tasks:
                    # здесь отправка задания через celery и/или уведомление менеджера
                    Result.objects.create(
                        participant_survey=participant_survey,
                        result=result_score,
                        is_send_task=True,
                    )
                else:
                    # уведомление менеджера
                    Result.objects.create(
                        participant_survey=participant_survey, result=result_score
                    )
            else:
                Result.objects.create(
                    participant_survey=participant_survey, result=result_score
                )
        return Response(status=status.HTTP_201_CREATED)

    @action(
        detail=True,
        url_path="get-question",
        methods=["get"],
        serializer_class=QuestionParticipantSerializer,
        permission_classes=[AllowAny],
    )
    def get_question(self, request, *args, **kwargs):
        """Получение нового вопроса на который еще не отвечали"""
        participant_survey = self.get_object()
        unanswered_questions = participant_survey.survey.questions.annotate(
            has_answer=Subquery(
                Answer.objects.filter(
                    participant_survey=participant_survey, question=OuterRef("pk")
                ).values("id")[:1]
            )
        ).filter(has_answer=None)
        unanswered_question = unanswered_questions.first()
        if unanswered_question:
            serializer = self.get_serializer(unanswered_question)
            return Response(serializer.data)
        else:
            return Response({"message": "All questions have been answered"})

    @action(
        detail=True,
        url_path="post-answer",
        methods=["post"],
        serializer_class=AnswerSerializer,
        permission_classes=[AllowAny],
    )
    def post_answer(self, request, *args, **kwargs):
        """Сохранение ответа на вопрос"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Answer.objects.create(
            participant_survey=serializer.validated_data["participant_survey"],
            question=serializer.validated_data["question"],
            option=serializer.validated_data["option"],
        )
        return Response(status=status.HTTP_201_CREATED)
