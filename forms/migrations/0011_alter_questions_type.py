# Generated by Django 5.0.4 on 2024-04-13 16:26
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    """ """

    dependencies = [
        ("forms", "0010_rename_question_type_questions_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questions",
            name="type",
            field=models.CharField(
                choices=[
                    ("radio", "Один вариант"),
                    ("checkbox", "Много вариантов"),
                    ("text", "Текст"),
                ],
                max_length=20,
            ),
        ),
    ]
