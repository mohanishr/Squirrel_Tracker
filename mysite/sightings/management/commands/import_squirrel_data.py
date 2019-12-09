
m django.core.management.base import BaseCommand
import pandas as pd
import csv
from sightings.models import Sighting
class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', nargs = '+', type = str)
                        
    def handle(self, *args, **kwargs):
        with open(kwargs['path'][0]) as file:
            reader = csv.DictReader(file)
            data = list(reader)
        for item in data:
            s = Sighting(
            x = item['x'],
            y = item['y'],
            unique_squirrel_id = item['unique_squirrel_id'],
            shift = item['shift'],
            date = item['date'],
            age = item['age'],
            primary_fur_color = item['primary_fur_color'],
            location = item['location'],
            specific_location = item['specific_location'],
            running = item['running'],
            climbing = item['climbing'],
            eating = item['eating'],
            foraging = item['foraging'],
            other_activities = item['other_activities'],
            kuks = item['kuks'],
            quaas = item['quaas'],
            moans = item['moans'],
            tail_flags = item['tail_flags'],
            tail_twitches = item['tail_twitches'],
            approaches = item['approaches'],
            indifferent = item['indifferent'],
            runs_from = item['runs_from'],
            )
            s.save()
