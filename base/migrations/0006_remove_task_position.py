# Generated by Django 5.0 on 2023-12-30 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_task_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='position',
        ),
    ]