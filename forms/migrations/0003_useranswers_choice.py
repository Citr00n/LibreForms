# Generated by Django 5.0.4 on 2024-04-12 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_rename_form_forms'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswers',
            name='choice',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='forms.choices'),
            preserve_default=False,
        ),
    ]
