# apps/flights/models.py
from django.db import models
class Airport(models.Model):
    icao_code = models.CharField(max_length=4, unique=True)
    iata_code = models.CharField(max_length=3, unique=True, null=True, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    abbreviated_name = models.CharField(max_length=50, null=True, blank=True)
    altitude = models.IntegerField(help_text="In feet")
    runway_length = models.IntegerField(help_text="In metres")
    runway_width = models.IntegerField(help_text="In metres")
    tower_frequency = models.CharField(max_length=100, help_text="In MHz. If more than 1, separate by |, e.g. 131,5|879,5|987,5")
    acc_frequency = models.CharField(max_length=100, help_text="In KHz. If more than 1, separate by |, e.g. 1315|8795|9875")
    # adjacent_acc = 
    # lighting_system
    # navigation_systems
    # radar frequency
    # etc

    def __str__(self):
        return f"{self.abbreviated_name} ({self.icao_code})"

