from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from sightings.models import Sighting


def index(request):
    sightings = Sighting.objects.all()
    template = loader.get_template('map/map.html')
    context = {'sightings':sightings}
    return HttpResponse(template.render(context, request))
# Create your views here.
