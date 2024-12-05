from django.shortcuts import render, get_object_or_404
from airports.models import Airport, METAR, TAF, SIGMET, NOTAM, Alert

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

def notam_list(request):
    notams = NOTAM.objects.all()
    context = {
        "notams": notams
    }
    return render(request, 'airports/notam_list.html', context)

def notam_detail(request, pk):
    notam = get_object_or_404(NOTAM, pk=pk)
    context = {
        "notam": notam
    }
    return render(request, 'airports/notam_detail.html', context)

def alert_list(request):
    alerts = Alert.objects.filter(active=True).order_by('-timestamp')
    return render(request, 'airports/alerts_list.html', {'alerts': alerts})

def alert_detail(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    return render(request, 'airports/alert_detail.html', {'alert': alert})

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import METAR, TAF, SIGMET
from .forms import METARForm, TAFForm, SIGMETForm, NOTAMForm

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

class NOTAMCreateView(CreateView):
    model = NOTAM
    form_class = NOTAMForm
    template_name = 'notam_create.html'
    success_url = reverse_lazy('notam_detail')
