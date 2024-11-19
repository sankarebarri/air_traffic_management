# Generated by Django 5.1.3 on 2024-11-19 17:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0002_alter_airport_tower_frequency'),
    ]

    operations = [
        migrations.CreateModel(
            name='METAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('temperature', models.FloatField(help_text='Temperature in Celsius')),
                ('wind_speed', models.FloatField(help_text='Wind speed in knots')),
                ('wind_direction', models.IntegerField(help_text='Wind direction in degrees')),
                ('visibility', models.FloatField(help_text='Visibility in meters')),
                ('cloud_coverage', models.CharField(blank=True, help_text='Cloud coverage details (e.g., FEW, BKN, OVC)', max_length=50, null=True)),
                ('precipitation', models.CharField(blank=True, help_text='Type of precipitation (e.g., Rain, Snow, None)', max_length=50, null=True)),
                ('pressure', models.FloatField(help_text='Pressure in hPa')),
                ('remarks', models.TextField(blank=True, help_text='Additional remarks or observations', null=True)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='metar_reports', to='airports.airport')),
            ],
        ),
        migrations.CreateModel(
            name='SIGMET',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField(help_text='End of SIGMET validity')),
                ('phenomenon', models.CharField(help_text='Weather phenomenon (e.g., Thunderstorm, Turbulence, Volcanic Ash)', max_length=100)),
                ('severity', models.CharField(choices=[('Light', 'Light'), ('Moderate', 'Moderate'), ('Severe', 'Severe')], max_length=50)),
                ('affected_area', models.TextField(help_text='Coordinates or description of affected area')),
                ('remarks', models.TextField(blank=True, help_text='Additional details about the SIGMET', null=True)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sigmet_alerts', to='airports.airport')),
            ],
        ),
        migrations.CreateModel(
            name='TAF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateTimeField(help_text='Start of forecast validity')),
                ('valid_to', models.DateTimeField(help_text='End of forecast validity')),
                ('temperature_max', models.FloatField(help_text='Maximum temperature in Celsius')),
                ('temperature_min', models.FloatField(help_text='Minimum temperature in Celsius')),
                ('wind_speed', models.FloatField(help_text='Wind speed in knots')),
                ('wind_direction', models.IntegerField(help_text='Wind direction in degrees')),
                ('visibility', models.FloatField(help_text='Visibility in meters')),
                ('cloud_coverage', models.CharField(blank=True, help_text='Cloud coverage details (e.g., FEW, BKN, OVC)', max_length=50, null=True)),
                ('precipitation', models.CharField(blank=True, help_text='Type of precipitation (e.g., Rain, Snow, None)', max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, help_text='Additional remarks or forecast details', null=True)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taf_reports', to='airports.airport')),
            ],
        ),
    ]
