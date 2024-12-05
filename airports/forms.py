from django import forms
from .models import METAR, TAF, SIGMET, NOTAM

class METARForm(forms.ModelForm):
    class Meta:
        model = METAR
        fields = '__all__'

class TAFForm(forms.ModelForm):
    class Meta:
        model = TAF
        fields = '__all__'

class SIGMETForm(forms.ModelForm):
    class Meta:
        model = SIGMET
        fields = '__all__'

class NOTAMForm(forms.ModelForm):
    class Meta:
        model = NOTAM
        fields = '__all__'
