# Generated by Django 3.2.5 on 2021-12-03 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itembank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='answer_order',
        ),
    ]
