# Generated by Django 3.2.5 on 2021-12-23 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizecesubject',
            name='fail_mark',
        ),
        migrations.RemoveField(
            model_name='quizecesubject',
            name='pass_mark',
        ),
        migrations.RemoveField(
            model_name='quizecesubject',
            name='stored_score',
        ),
        migrations.RemoveField(
            model_name='quizecesubject',
            name='success_mark',
        ),
    ]
