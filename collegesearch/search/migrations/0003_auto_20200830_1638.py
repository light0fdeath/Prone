# Generated by Django 3.1 on 2020-08-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20200830_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='Actual_Duration',
            field=models.TextField(default='a', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='college',
            name='Actual_Fees',
            field=models.TextField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='college',
            name='Course_Name',
            field=models.CharField(blank=True, choices=[('VET-Diploma', 'VET-Diploma'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PHD', 'PHD')], max_length=200),
        ),
        migrations.AddField(
            model_name='college',
            name='Duration',
            field=models.CharField(blank=True, choices=[('0-6 Months', '0-6 Months'), ('6 Months - 1 Year', '6 Months - 1 Year'), ('1-2 Years', '1-2 Years'), ('> 2 Years', '> 2 Years')], max_length=100),
        ),
        migrations.AddField(
            model_name='college',
            name='Fees',
            field=models.CharField(blank=True, choices=[('< $5000 Per Year', '< $5000 Per Year'), ('$5000-$10000 Per Year', '$5000-$10000 Per Year'), ('$10000-$20000 Per Year', '$10000-$20000 Per Year'), ('> $20000 Per Year', '> $20000 Per Year')], max_length=100),
        ),
        migrations.AddField(
            model_name='college',
            name='Location',
            field=models.CharField(blank=True, choices=[('New South Wales', 'New South Wales'), ('Queensland', 'Queensland'), ('South Australia', 'South Australia'), ('Tasmania', 'Tasmania'), ('Victoria', 'Victoria'), ('Queensland', 'Queensland'), ('Western Australia', 'Western Australia'), ('Australian Capital Territory', 'Australian Capital Territory'), ('Northern Territory', 'Northern Territory')], max_length=200),
        ),
        migrations.AddField(
            model_name='college',
            name='University',
            field=models.CharField(blank=True, choices=[('Western Sydney Uni', 'Western Sydney Uni'), ('University of Wollonggong', 'University of Wollonggong')], max_length=200),
        ),
    ]
