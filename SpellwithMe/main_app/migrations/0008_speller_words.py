# Generated by Django 5.1 on 2024-08-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_name_word_word_word_color_alter_word_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='speller',
            name='words',
            field=models.ManyToManyField(to='main_app.word'),
        ),
    ]
