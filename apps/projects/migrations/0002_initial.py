# Generated by Django 5.0.3 on 2024-04-10 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.task'),
        ),
    ]