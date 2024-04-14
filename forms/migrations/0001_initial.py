# Generated by Django 5.0.4 on 2024-04-14 17:10

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=10000)),
                ('confirmationMsg', models.TextField(blank=True,
                 default='Ваш ответ был засчитан.', max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('only_logged_in', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Форма',
                'verbose_name_plural': 'Формы',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False, unique=True)),
                ('question', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=10000)),
                ('type', models.CharField(choices=[('radio', 'Один вариант'), (
                    'checkbox', 'Много вариантов'), ('text', 'Текст')], max_length=20)),
                ('required', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='questions', to='forms.forms')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False, unique=True)),
                ('choice', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='choices', to='forms.questions')),
            ],
            options={
                'verbose_name': 'Вариант ответа',
                'verbose_name_plural': 'Варианты ответа',
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False,
                 primary_key=True, serialize=False, unique=True)),
                ('choice', models.TextField(max_length=10000)),
                ('session_id', models.UUIDField(editable=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                 related_name='answers', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 related_name='answers', to='forms.questions')),
            ],
        ),
    ]
