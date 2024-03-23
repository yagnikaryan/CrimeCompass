from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.template import loader
from .forms import RouteForm
import requests



# Create your views here.

def index(request):
    template = loader.get_template('map.html')
    return HttpResponse(template.render())

def map(request):
    # Retrieve the data from the session
    starting_location = request.session.get('starting_location', 'Not specified')
    destination = request.session.get('destination', 'Not specified')

    # Pass the locations to the map template
    context = {
        'starting_location': starting_location,
        'destination': destination
    }
    return render(request, 'map.html', context)


def home(request):
    form = RouteForm()
    return render(request, 'home.html', {'form': form})



def submit_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            # Save the form data to the session
            request.session['starting_location'] = form.cleaned_data['starting_location']
            request.session['destination'] = form.cleaned_data['destination']

            # Redirect to the map views
            return redirect('map')
    else:
        form = RouteForm()
    return render(request, 'home.html', {'form': form})