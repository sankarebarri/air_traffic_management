# Generated by Django 5.1.3 on 2024-11-07 08:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_sign', models.CharField(max_length=20, unique=True)),
                ('registration_number', models.CharField(max_length=50, unique=True)),
                ('aircraft_type', models.CharField(max_length=10)),
                ('aircraft_speed', models.IntegerField(help_text='Speed in knots')),
                ('turbulence_category', models.CharField(choices=[('Heavy', 'H'), ('Medium', 'M'), ('Light', 'L')], help_text='Turbulence category: H (Heavy), M (Medium), L (Light)', max_length=6)),
                ('routes', models.TextField(help_text='Route(s) to be followed')),
                ('flight_level_requested', models.IntegerField(help_text='Requested flight level in feet')),
                ('squawk', models.CharField(blank=True, help_text='Radar detection code (optional)', max_length=4, null=True)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Delayed', 'Delayed'), ('Departed', 'Departed'), ('Arrived', 'Arrived'), ('Cancelled', 'Cancelled')], max_length=20)),
                ('arrival_airport', models.ForeignKey(help_text='Arrival airport ICAO code', on_delete=django.db.models.deletion.PROTECT, related_name='arrivals', to='airports.airport')),
                ('departure_airport', models.ForeignKey(help_text='Departure airport ICAO code', on_delete=django.db.models.deletion.PROTECT, related_name='departures', to='airports.airport')),
                ('deviation_airports', models.ManyToManyField(blank=True, related_name='deviation_airports', to='airports.airport')),
            ],
        ),
    ]
