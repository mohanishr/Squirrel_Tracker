from django.db import models
from django.utils.translation import gettext as _
class Sighting(models.Model):
    x =models.FloatField(max_length = 200, default = 0.0)
    y = models.FloatField(max_length=200, default = 0.0)
    unique_squirrel_id = models.CharField(max_length=200)
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = (
            (AM, 'AM'),
            (PM, 'PM'),
            )
    shift = models.CharField(
            max_length = 2,
            choices = SHIFT_CHOICES,
            default = AM,
            )
    date = models.IntegerField(
            help_text = _('MMDDYYYY'),
            default = 0,
            )
    ADULT = 'adult'
    JUVENILE = 'juvenile'

    AGE_CHOICES = (
            (ADULT, 'ADULT'),
            (JUVENILE, 'JUVENILE'),
            )
    
    age = models.CharField(
            max_length = 100,
            choices = AGE_CHOICES,
            default = ADULT,
            )
    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    FUR_COLORS = (
            (GRAY, 'Gray'),
            (CINNAMON, 'Cinnamon'),
            (BLACK, 'Black'),
            )

    primary_fur_color = models.CharField(
            max_length = 100,
            choices = FUR_COLORS,
            default = BLACK,
            )

    GROUND_PLANE = 'Ground Plane'
    ABOVE_GROUND = 'Above Ground'
    LOCATION_CHOICES = (
            (GROUND_PLANE, 'Ground Plane'),
            (ABOVE_GROUND, 'Above Ground'),
            )
    location = models.CharField(
            max_length = 20,
            choices = LOCATION_CHOICES,
            default = GROUND_PLANE,
            )
    specific_location = models.CharField(max_length= 200)

    running = models.BooleanField(default=False)
    chasing = models.BooleanField(default=False)
    climbing= models.BooleanField(default=False)
    eating = models.BooleanField(default=False)
    foraging = models.BooleanField(default=False)
    other_activities = models.CharField(max_length = 200)
    kuks = models.BooleanField(default=False)
    quaas = models.BooleanField(default=False)
    moans = models.BooleanField(default=False)
    tail_flags = models.BooleanField(default=False)
    tail_twitches = models.BooleanField(default=False)
    approaches = models.BooleanField(default=False)
    indifferent = models.BooleanField(default=False)
    runs_from = models.BooleanField(default=False)
    def __str__(self):
        return ('%s' %(self.unique_squirrel_id))
# Create your models here.
