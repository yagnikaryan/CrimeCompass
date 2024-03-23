# forms.py
from django import forms

class RouteForm(forms.Form):
    starting_location = forms.CharField(label='Starting Location', max_length=100)
    destination = forms.CharField(label='Destination', max_length=100)
