# Generated by Django 4.2 on 2023-05-12 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
