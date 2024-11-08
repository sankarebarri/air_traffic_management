from django.db import models
from airports.models import Airport

class Flights(models.Model):
    call_sign = models.CharField(max_length=20, unique=True)
    registration_number = models.CharField(max_length=50, unique=True)
    aircraft_type = models.CharField(max_length=10)
    aircraft_speed = models.IntegerField(help_text="Speed in knots") 
    turbulence_category = models.CharField(
        max_length=6, 
        choices=[('Heavy', 'H'), ('Medium', 'M'), ('Light', 'L')],
        help_text="Turbulence category: H (Heavy), M (Medium), L (Light)"
    )

    routes = models.TextField(help_text="Route(s) to be followed")
    flight_level_requested = models.IntegerField(help_text="Requested flight level in feet")
    squawk = models.CharField(max_length=4, null=True, blank=True, help_text="Radar detection code (optional)")
    deviation_airports = models.ManyToManyField(Airport, related_name='deviation_airports', blank=True)
    departure_airport = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='departures', help_text="Departure airport ICAO code")
    arrival_airport = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='arrivals', help_text="Arrival airport ICAO code")
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(
        max_length=20, 
        choices=[('Scheduled', 'Scheduled'), ('Delayed', 'Delayed'), ('Departed', 'Departed'), ('Arrived', 'Arrived'), ('Cancelled', 'Cancelled')]
    )

    regime = models.CharField(
        max_length=10, 
        choices=[('Private', 'Private'), ('Military', 'Military'), ('Commercial', 'Commercial')],
        default='Commercial',
        help_text="Type of flight regime"
    )
    
    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'
    def __str__(self):
        return f"{self.call_sign} ({self.departure_airport} -> {self.arrival_airport})"
