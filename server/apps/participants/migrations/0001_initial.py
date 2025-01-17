# Generated by Django 4.2.13 on 2024-06-20 13:51

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('surveys', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта')),
                ('hh', models.CharField(blank=True, max_length=255, verbose_name='Ссылка на резюме')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='ParticipantSurvey',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='UUID')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_surveys', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='participants.participant', verbose_name='Участник')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='surveys.survey', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Участник и опрос',
                'verbose_name_plural': 'Участники и опросы',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('result', models.IntegerField(default=0, verbose_name='Результат')),
                ('is_send_task', models.BooleanField(blank=True, default=False, null=True, verbose_name='Отправлено задание')),
                ('participant_survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='participants.participantsurvey', verbose_name='Связь участника и опроса')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys.option', verbose_name='Вариант ответа')),
                ('participant_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='participants.participantsurvey', verbose_name='Связь участника и опроса')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='surveys.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.AddConstraint(
            model_name='participantsurvey',
            constraint=models.UniqueConstraint(fields=('participant', 'survey'), name='unique_participant_and_survey'),
        ),
        migrations.AddConstraint(
            model_name='answer',
            constraint=models.UniqueConstraint(fields=('participant_survey', 'question'), name='unique_participant_survey_and_question'),
        ),
    ]
