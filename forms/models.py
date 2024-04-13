import uuid

from django.contrib.auth.models import User
from django.db import models


class Forms(models.Model):
    """ """

    class Meta:
        """ """

        verbose_name = "Форма"
        verbose_name_plural = "Формы"

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=10000)
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name="creator")
    confirmationMsg = models.TextField(max_length=255,
                                       default="Ваш ответ был засчитан.",
                                       blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    only_logged_in = models.BooleanField(default=False)


class Questions(models.Model):

    question_types = {
        'radio': 'Один вариант',
        'checkbox': 'Много вариантов',
        'text': 'Текст',
    }
    """ """

    class Meta:
        """ """

        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True)
    question = models.CharField(max_length=200)
    description = models.TextField(blank=True, max_length=10000)
    type = models.CharField(max_length=20, choices=question_types)
    form = models.ForeignKey(Forms,
                             on_delete=models.CASCADE,
                             related_name="questions")
    required = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class Choices(models.Model):
    """ """

    class Meta:
        """ """

        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True)
    question = models.ForeignKey(Questions,
                                 on_delete=models.CASCADE,
                                 related_name="choices")
    choice = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class UserAnswers(models.Model):
    """ """

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choices, on_delete=models.CASCADE)


# Форма <-- Много вопросов
# Вопрос <-- Много вариантов
# На одну форму по несколько строк вопросов   | Благодаря uuid
# На один вопрос по несколько строк вариантов |
#
