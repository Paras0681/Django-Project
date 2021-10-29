# Generated by Django 3.2.8 on 2021-10-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_info',
            name='incident_location',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='report_info',
            name='incident_types',
            field=models.CharField(choices=[('E', 'Environmental incident'), ('I', 'Injury'), ('P', 'Property damage'), ('V', 'Vehicle'), ('O', 'Other')], max_length=2),
        ),
    ]