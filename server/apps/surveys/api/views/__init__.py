from server.apps.surveys.api.views.survey import SurveyViewSet
from server.apps.surveys.api.views.question import QuestionViewSet
from server.apps.surveys.api.views.option import OptionViewSet
from server.apps.surveys.api.views.task import TaskViewSet

__all__ = [
    'SurveyViewSet',
    'QuestionViewSet',
    'TaskViewSet',
    'OptionViewSet'
]
