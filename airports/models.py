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



from django.db import models
from airports.models import Airport
from django.utils.timezone import now

class METAR(models.Model):
    """Model for current weather conditions (METAR)."""
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="metar_reports")
    observation_time = models.DateTimeField(default=now)
    temperature = models.FloatField(help_text="Temperature in Celsius")
    wind_speed = models.FloatField(help_text="Wind speed in knots")
    wind_direction = models.IntegerField(help_text="Wind direction in degrees")
    visibility = models.FloatField(help_text="Visibility in meters")
    cloud_coverage = models.CharField(
        max_length=50,
        help_text="Cloud coverage details (e.g., FEW, BKN, OVC)",
        blank=True,
        null=True
    )
    precipitation = models.CharField(
        max_length=50,
        help_text="Type of precipitation (e.g., Rain, Snow, None)",
        blank=True,
        null=True
    )
    pressure = models.FloatField(help_text="Pressure in hPa")
    remarks = models.TextField(help_text="Additional remarks or observations", blank=True, null=True)

    def __str__(self):
        return f"METAR: {self.airport.icao_code} at {self.observation_time.strftime('%Y-%m-%d %H:%M')}"

class TAF(models.Model):
    """Model for weather forecasts (TAF)."""
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="taf_reports")
    valid_from = models.DateTimeField(help_text="Start of forecast validity")
    valid_to = models.DateTimeField(help_text="End of forecast validity")
    temperature_max = models.FloatField(help_text="Maximum temperature in Celsius")
    temperature_min = models.FloatField(help_text="Minimum temperature in Celsius")
    wind_speed = models.FloatField(help_text="Wind speed in knots")
    wind_direction = models.IntegerField(help_text="Wind direction in degrees")
    visibility = models.FloatField(help_text="Visibility in meters")
    cloud_coverage = models.CharField(
        max_length=50,
        help_text="Cloud coverage details (e.g., FEW, BKN, OVC)",
        blank=True,
        null=True
    )
    precipitation = models.CharField(
        max_length=50,
        help_text="Type of precipitation (e.g., Rain, Snow, None)",
        blank=True,
        null=True
    )
    remarks = models.TextField(help_text="Additional remarks or forecast details", blank=True, null=True)

    def __str__(self):
        return f"TAF: {self.airport.icao_code} ({self.valid_from.strftime('%Y-%m-%d %H:%M')} - {self.valid_to.strftime('%Y-%m-%d %H:%M')})"

class SIGMET(models.Model):
    """Model for significant weather alerts (SIGMET)."""
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="sigmet_alerts")
    issued_at = models.DateTimeField(default=now)
    valid_until = models.DateTimeField(help_text="End of SIGMET validity")
    phenomenon = models.CharField(
        max_length=100,
        help_text="Weather phenomenon (e.g., Thunderstorm, Turbulence, Volcanic Ash)"
    )
    severity = models.CharField(
        max_length=50,
        choices=[
            ("Light", "Light"),
            ("Moderate", "Moderate"),
            ("Severe", "Severe"),
        ]
    )
    affected_area = models.TextField(help_text="Coordinates or description of affected area")
    remarks = models.TextField(help_text="Additional details about the SIGMET", blank=True, null=True)

    def __str__(self):
        return f"SIGMET: {self.phenomenon} ({self.severity}) - {self.airport.icao_code}"
