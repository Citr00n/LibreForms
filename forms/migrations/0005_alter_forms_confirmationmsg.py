# Generated by Django 5.0.4 on 2024-04-12 14:14
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    """ """

    dependencies = [
        ("forms", "0004_alter_forms_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="forms",
            name="confirmationMsg",
            field=models.TextField(default="Ваш ответ был засчитан.", max_length=255),
        ),
    ]
