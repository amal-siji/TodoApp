# Generated by Django 4.2 on 2023-05-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
