# Generated by Django 3.1 on 2020-08-30 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('University', models.CharField(blank=True, choices=[('Western Sydney Uni', 'Western Sydney Uni'), ('University of Wollonggong', 'University of Wollonggong')], max_length=200)),
                ('Course_Name', models.CharField(blank=True, choices=[('VET-Diploma', 'VET-Diploma'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('PHD', 'PHD')], max_length=200)),
                ('Actual_Course_Name', models.CharField(max_length=200)),
                ('Location', models.CharField(blank=True, choices=[('New South Wales', 'New South Wales'), ('Queensland', 'Queensland'), ('South Australia', 'South Australia'), ('Tasmania', 'Tasmania'), ('Victoria', 'Victoria'), ('Queensland', 'Queensland'), ('Western Australia', 'Western Australia'), ('Australian Capital Territory', 'Australian Capital Territory'), ('Northern Territory', 'Northern Territory')], max_length=200)),
                ('Fees', models.CharField(blank=True, choices=[('< $5000 Per Year', '< $5000 Per Year'), ('$5000-$10000 Per Year', '$5000-$10000 Per Year'), ('$10000-$20000 Per Year', '$10000-$20000 Per Year'), ('> $20000 Per Year', '> $20000 Per Year')], max_length=100)),
                ('Actual_Fees', models.TextField(max_length=200)),
                ('Duration', models.CharField(blank=True, choices=[('0-6 Months', '0-6 Months'), ('6 Months - 1 Year', '6 Months - 1 Year'), ('1-2 Years', '1-2 Years'), ('> 2 Years', '> 2 Years')], max_length=100)),
                ('Actual_Duration', models.TextField(max_length=200)),
            ],
        ),
    ]