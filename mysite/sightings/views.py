from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sighting


def index(request):
    sq_data = Sighting.objects.all()
    template = loader.get_template('sightings/index.html')
    context = {
                'sq_data': sq_data,
                }
    return HttpResponse(template.render(context, request))

# Create your views here.
