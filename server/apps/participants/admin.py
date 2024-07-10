from django.contrib import admin

from server.apps.participants.models import (
    Answer,
    Participant,
    ParticipantSurvey,
    Result,
)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "question",
        "option",
    ]
    list_select_related = [
        "question",
        "option",
    ]
    list_filter = ["question", "option"]
    search_fields = ["question__title", "option__title"]


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "surname", "email"]
    list_filter = ["name", "surname", "email"]
    search_fields = ["name", "surname", "email"]


@admin.register(ParticipantSurvey)
class ParticipantSurveyAdmin(admin.ModelAdmin):
    list_display = ["uuid", "creator", "participant", "survey"]
    list_select_related = ["creator", "participant", "survey"]
    list_filter = ["creator", "participant", "survey"]
    search_fields = ["creator__username", "participant__name", "survey__title"]


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ["id", "result", "is_send_task"]
    list_filter = ["is_send_task"]
    search_fields = ["result"]
