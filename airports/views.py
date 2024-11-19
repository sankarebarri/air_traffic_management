from django.shortcuts import render
from airports.models import Airport, METAR, TAF, SIGMET

def weather_reports_view(request):
    airports = Airport.objects.all()  # Fetch all airports
    weather_data = []

    for airport in airports:
        # Fetch the latest METAR, TAF, and SIGMET for the airport
        metar = airport.metar_reports.order_by('-observation_time').first()
        taf = airport.taf_reports.order_by('-valid_from').first()
        sigmet = airport.sigmet_alerts.order_by('-issued_at').first()

        # Append weather data to the list
        weather_data.append({
            "airport": airport,
            "metar": metar,
            "taf": taf,
            "sigmet": sigmet,
        })

    return render(request, 'airports/weather_reports.html', {'weather_data': weather_data})


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import METAR, TAF, SIGMET
from .forms import METARForm, TAFForm, SIGMETForm

class METARCreateView(CreateView):
    model = METAR
    form_class = METARForm
    template_name = 'airports/metar_create.html'
    success_url = reverse_lazy('weather_reports')

class TAFCreateView(CreateView):
    model = TAF
    form_class = TAFForm
    template_name = 'taf_create.html'
    success_url = reverse_lazy('weather_reports')

class SIGMETCreateView(CreateView):
    model = SIGMET
    form_class = SIGMETForm
    template_name = 'sigmet_create.html'
    success_url = reverse_lazy('weather_reports')
