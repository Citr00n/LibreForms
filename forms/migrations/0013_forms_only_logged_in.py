# Generated by Django 5.0.4 on 2024-04-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):
    """ """

    dependencies = [
        ("forms", "0012_questions_required"),
    ]

    operations = [
        migrations.AddField(
            model_name="forms",
            name="only_logged_in",
            field=models.BooleanField(default=False),
        ),
    ]
