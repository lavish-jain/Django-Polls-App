# Generated by Django 3.0.1 on 2020-01-01 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choiceText',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='pubDate',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='questionText',
            new_name='question_text',
        ),
    ]
