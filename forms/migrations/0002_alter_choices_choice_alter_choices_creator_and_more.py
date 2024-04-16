# Generated by Django 5.0.4 on 2024-04-16 18:28

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='choices',
            name='choice',
            field=models.CharField(help_text='При типе вопроса "Текст" создавать вариант ответа не нужно (он проигнорируется системой)',
                                   max_length=200, verbose_name='Вариант ответа'),
        ),
        migrations.AlterField(
            model_name='choices',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='choices',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False,
                                   primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='choices',
            name='question',
            field=models.ForeignKey(help_text='Вопрос, к которому относится вариант ответа',
                                    on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='forms.questions', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='confirmationMsg',
            field=models.TextField(blank=True, default='Ваш ответ был засчитан.',
                                   help_text='Сообщение, показывающееся при отправке формы', max_length=255, verbose_name='Завершающее сообщение'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='createdAt',
            field=models.DateTimeField(
                auto_now_add=True, verbose_name='Форма создана'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Создатель формы'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='description',
            field=models.TextField(
                blank=True, max_length=10000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False,
                                   help_text='Ваша форма будет доступна по ссылке /form/{ID}/', primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='only_logged_in',
            field=models.BooleanField(
                default=False, verbose_name='Разрешить только авторизованным'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='title',
            field=models.CharField(
                max_length=255, verbose_name='Название формы'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='updatedAt',
            field=models.DateTimeField(
                auto_now=True, verbose_name='Форма обновлена последний раз'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='description',
            field=models.TextField(
                blank=True, max_length=10000, verbose_name='Описание вопроса'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='form',
            field=models.ForeignKey(help_text='Форма, к которой относится вопрос', on_delete=django.db.models.deletion.CASCADE,
                                    related_name='questions', to='forms.forms', verbose_name='Форма'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False,
                                   primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(max_length=200, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='required',
            field=models.BooleanField(
                default=False, help_text='Не работает при типе вопроса "Много вариантов"', verbose_name='Обязателен'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='type',
            field=models.CharField(choices=[('radio', 'Один вариант'), ('checkbox', 'Много вариантов'), ('text', 'Текст')],
                                   help_text='При типе вопроса "Текст" создавать вариант ответа не нужно (он проигнорируется системой)', max_length=20, verbose_name='Тип вопроса'),
        ),
    ]
