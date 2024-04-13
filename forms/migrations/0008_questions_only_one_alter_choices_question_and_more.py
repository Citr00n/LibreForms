# Generated by Django 5.0.4 on 2024-04-13 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_alter_choices_options_alter_forms_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='only_one',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='choices',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='forms.questions'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='forms.forms'),
        ),
    ]
