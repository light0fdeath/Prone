# Generated by Django 3.1 on 2020-08-30 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='Actual_Duration',
        ),
        migrations.RemoveField(
            model_name='college',
            name='Actual_Fees',
        ),
        migrations.RemoveField(
            model_name='college',
            name='Course_Name',
        ),
        migrations.RemoveField(
            model_name='college',
            name='Duration',
        ),
        migrations.RemoveField(
            model_name='college',
            name='Fees',
        ),
        migrations.RemoveField(
            model_name='college',
            name='Location',
        ),
        migrations.RemoveField(
            model_name='college',
            name='University',
        ),
    ]
