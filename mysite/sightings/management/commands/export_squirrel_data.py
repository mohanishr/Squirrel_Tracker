from django.core.management.base import BaseCommand
import pandas as pd
#from . import import_squirrel_data
import csv
from sightings.models import Sighting
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', nargs = '+', type = str)
                        
    def handle(self, *args, **kwargs):
        path = kwargs['path'][0]
        s = Sighting.objects.all()
        df = pd.DataFrame(s.values())
        df.to_csv(path)
