# Generated by Django 5.0.3 on 2024-04-17 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_owner_task_is_complete_task_user_completed_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user_completed',
            new_name='user',
        ),
    ]
