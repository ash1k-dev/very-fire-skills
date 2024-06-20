from rest_framework.routers import SimpleRouter

from server.apps.companies.api.views import CompanyViewSet, SubscriptionViewSet
from server.apps.participants.api.views import AnswerViewSet, ParticipantSurveyViewSet, ResultViewSet
from server.apps.surveys.api.views import SurveyViewSet, QuestionViewSet, OptionViewSet, TaskViewSet


app_name = 'api'

router = SimpleRouter()

router.register(r"companies", CompanyViewSet, basename="companies")
router.register(r"subscriptions", SubscriptionViewSet, basename="subscriptions")
router.register(r"participants", ParticipantSurveyViewSet, basename="participants")
router.register(r"results", ResultViewSet, basename="results")
router.register(r"answers", AnswerViewSet, basename="answers")
router.register(r"surveys", SurveyViewSet, basename="surveys")
router.register(r"questions", QuestionViewSet, basename="questions")
router.register(r"options", OptionViewSet, basename="options")
router.register(r"tasks", TaskViewSet, basename="tasks")

urlpatterns = router.urls
