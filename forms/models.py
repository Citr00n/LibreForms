import uuid

from django.contrib.auth.models import User
from django.db import models


class Forms(models.Model):
    """ """

    class Meta:
        """ """

        verbose_name = "Форма"
        verbose_name_plural = "Формы"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="ID",
        help_text="Ваша форма будет доступна по ссылке /form/{ID}/",
    )
    title = models.CharField(max_length=255, verbose_name="Название формы")
    description = models.TextField(
        blank=True, max_length=10000, verbose_name="Описание"
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="creator",
        verbose_name="Создатель формы",
    )
    confirmationMsg = models.TextField(
        max_length=255,
        default="Ваш ответ был засчитан.",
        blank=True,
        verbose_name="Завершающее сообщение",
        help_text="Сообщение, показывающееся при отправке формы",
    )
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Форма создана")
    updatedAt = models.DateTimeField(
        auto_now=True, verbose_name="Форма обновлена последний раз"
    )
    only_logged_in = models.BooleanField(
        default=False, verbose_name="Разрешить только авторизованным"
    )

    def __str__(self):
        return f"{self.title}"


class Questions(models.Model):
    """ """

    question_types = {
        "radio": "Один вариант",
        "checkbox": "Много вариантов",
        "text": "Текст",
    }
    """ """

    class Meta:
        """ """

        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="ID",
    )
    question = models.CharField(max_length=200, verbose_name="Вопрос")
    description = models.TextField(
        blank=True, max_length=10000, verbose_name="Описание вопроса"
    )
    type = models.CharField(
        max_length=20,
        choices=question_types,
        verbose_name="Тип вопроса",
        help_text='При типе вопроса "Текст" создавать вариант ответа не нужно (он проигнорируется системой)',
    )
    form = models.ForeignKey(
        Forms,
        on_delete=models.CASCADE,
        related_name="questions",
        verbose_name="Форма",
        help_text="Форма, к которой относится вопрос",
    )
    required = models.BooleanField(
        default=False,
        verbose_name="Обязателен",
        help_text='Не работает при типе вопроса "Много вариантов"',
    )
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель"
    )

    def __str__(self):
        return f"{self.question} ({self.form}) [{self.question_types[self.type]}]"


class Choices(models.Model):
    """ """

    class Meta:
        """ """

        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответа"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="ID",
    )
    question = models.ForeignKey(
        Questions,
        on_delete=models.CASCADE,
        related_name="choices",
        verbose_name="Вопрос",
        help_text="Вопрос, к которому относится вариант ответа",
    )
    choice = models.CharField(
        max_length=200,
        verbose_name="Вариант ответа",
        help_text='При типе вопроса "Текст" создавать вариант ответа не нужно (он проигнорируется системой)',
    )
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Создатель"
    )

    def __str__(self):
        return f"{self.choice} [{self.question.form.title}: {self.question.question} / {self.question.question_types[self.question.type]}]"


class Answers(models.Model):
    """ """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="answers"
    )
    question = models.ForeignKey(
        Questions, on_delete=models.CASCADE, related_name="answers"
    )
    choice = models.TextField(max_length=10000)
    session_id = models.UUIDField(editable=False)
