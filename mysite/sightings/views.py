from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sighting
from django.http import HttpResponseRedirect
from .forms import AddForm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from matplotlib import pylab
from pylab import *
import PIL, PIL.Image
from io import BytesIO
import pandas as pd

def index(request):
    sq_data = Sighting.objects.all()
    template = loader.get_template('sightings/index.html')
    context = {
                'sq_data': sq_data,
                }
    return HttpResponse(template.render(context, request))

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = AddForm()

    return render(request, 'sightings/add.html', {'form':form})

def sqid(request, usid):
    squirrel_data = Sighting.objects.get(unique_squirrel_id = usid) 
    if request.method == 'POST':
        form = AddForm(request.POST, instance=squirrel_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = AddForm(instance = squirrel_data)
    return render(request, 'sightings/update.html', {'form':form})

def stats(request):
    s=Sighting.objects.all().values()
    df=pd.DataFrame(s)
    df2=pd.read_csv('file.csv')
    df2.groupby('primary_fur_color').count()['x']
    explode=(0,0,0)
    labels='Black', 'Cinnamon', 'Gray'
    s=df2.groupby('primary_fur_color').count()['x'].sum()
    x1=(df2.groupby('primary_fur_color').count()['x'][0])/s*100
    x2=(df2.groupby('primary_fur_color').count()['x'][1])/s*100
    x3=(df2.groupby('primary_fur_color').count()['x'][2])/s*100
    sizes=[x1, x2, x3]
    lst=[df2.groupby('shift').count()['x'][f] for f in range(2)]
    x=['AM','PM']
    lst2=[df2.groupby('hectare').count().sort_values(by=['x'], ascending=False)['x'][f] for f in range(20)]
    lst3=[df2.groupby('hectare').count().sort_values(by=['x'], ascending=False).index[x] for x in range(20)]



    fig, axs = plt.subplots(2, 2, figsize=(30,15))
    matplotlib.pyplot.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=0.9, wspace=1.5, hspace=1.5)
    axs[0, 0].pie(sizes, explode=explode, labels=labels, radius=2, textprops={'fontsize': 30})
    axs[0, 1].bar(x, height=lst)
    axs[0, 1].title.set_text('Variation in shift sightings')
    axs[0, 1].set_xlabel('Shift')
    axs[0, 1].set_ylabel('Frequency of sightings')
    axs[1, 1].bar(lst3, height=lst2)
    #axs[1 ,1].xticks(rotation=90)


    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    return HttpResponse(buffer.getvalue(), content_type="image/png")
# Create your views here.
