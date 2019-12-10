from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Welcome to our Squirrel Tracker</h1><h2><a href="/map/">Click here to view map</a></h2><h2><a href="/sightings/">Click here to edit and view sightings</a></h2>')
