# Generated by Django 4.1.3 on 2022-12-05 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_asg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='done',
        ),
    ]
