# Generated by Django 5.0.4 on 2024-04-13 16:21
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    """ """

    dependencies = [
        ("forms", "0008_questions_only_one_alter_choices_question_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="questions",
            name="only_one",
        ),
        migrations.AlterField(
            model_name="questions",
            name="question_type",
            field=models.CharField(
                choices=[
                    ("Один вариант", "radio"),
                    ("Много вариантов", "checkbox"),
                    ("Текст", "text"),
                ],
                max_length=20,
            ),
        ),
    ]
