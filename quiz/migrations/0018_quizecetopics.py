# Generated by Django 3.2.5 on 2021-12-02 17:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_quizecesubject_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizECETopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, help_text='a description of the quiz', max_length=255, verbose_name='Description')),
                ('number_question', models.PositiveIntegerField(blank=True, help_text='Number of question to be answered', null=True, verbose_name='Number of questions')),
                ('stored_score', models.BooleanField(default=False, help_text='If yes, the result of eact attempt by the user will be stored', verbose_name='Score')),
                ('pass_mark', models.SmallIntegerField(blank=True, default=0, help_text='Percentage required to pass exam.', validators=[django.core.validators.MaxValueValidator(70)], verbose_name='Pass Mark')),
                ('success_mark', models.TextField(blank=True, help_text='Displayed if user passes', verbose_name='Success Text')),
                ('fail_mark', models.TextField(blank=True, help_text='Displayed if use fails.', verbose_name='Fail Text')),
                ('ece_subject', models.ForeignKey(max_length=90, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_ece_subjects', to='quiz.ecesubject', verbose_name='ECE Subject')),
                ('ece_topic', models.ForeignKey(max_length=90, on_delete=django.db.models.deletion.CASCADE, related_name='quiz_ecetopics', to='quiz.ecetopic', verbose_name='ECE Topics')),
            ],
            options={
                'verbose_name': ('EXAM IN ECE TOPICS',),
                'verbose_name_plural': 'EXAM IN ECE TOPICS',
            },
        ),
    ]
