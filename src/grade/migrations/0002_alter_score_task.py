# Generated by Django 5.1.3 on 2024-12-02 21:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
        ('task', '0002_alter_task_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='task',
            field=models.ForeignKey(error_messages={'blank': 'The task cannot be empty', 'does_not_exist': 'The task does not exist', 'invalid': 'Invalid value for the task', 'null': 'The task cannot be empty', 'required': 'The task is required'}, on_delete=django.db.models.deletion.CASCADE, related_name='score_task', to='task.task'),
        ),
    ]
