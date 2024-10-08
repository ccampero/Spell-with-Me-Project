# Generated by Django 5.1 on 2024-08-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_spellers_speller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('minutes', models.IntegerField()),
                ('adulthelp', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=('Y', 'Yes'), max_length=1)),
            ],
        ),
    ]
