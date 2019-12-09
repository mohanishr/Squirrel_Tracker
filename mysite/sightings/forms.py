from django import forms
from django.forms import ModelForm
from sightings.models import Sighting
from django.forms import modelformset_factory

class AddForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
