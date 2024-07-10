from django.contrib import admin

from server.apps.surveys.models import Option, Question, Survey, Task


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    """Панель управления тестами"""

    list_display = ("id", "title", "passing_score", "time_limit")
    list_filter = ("title",)
    search_fields = ["title"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Панель управления вопросами"""

    list_display = (
        "id",
        "survey",
        "question_weight",
    )
    list_select_related = ("survey",)
    list_filter = ("survey",)
    search_fields = ["survey"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Панель управления заданиями"""

    list_display = (
        "id",
        "survey",
        "title",
    )
    list_select_related = ("survey",)
    list_filter = ("survey",)
    search_fields = ["survey"]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    """Панель управления вариантами ответа"""

    list_display = ("id", "question", "is_correct")
    list_select_related = ["question"]
    list_filter = ["question"]
    search_fields = ["question"]
