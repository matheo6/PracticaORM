# Generated by Django 5.0.3 on 2024-04-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_comment_priority_alter_member_rol_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='priority',
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('HG', 'Hight'), ('Md', 'Medium'), ('Lw', 'Low')], default='LW', max_length=120),
        ),
    ]
