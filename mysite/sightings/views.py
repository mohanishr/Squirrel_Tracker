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
    lst2=[]
    lst2.append(df2.groupby('age').count().loc['Adult']['x'])
    lst2.append(df2.groupby('age').count().loc['Juvenile']['x'])
    lst3=['Adult', 'Juvenile']
    ground=['Above \n'+'Ground', 'Below \n'+'Ground']
    lst4=[df2.groupby('location').count()['x'][f] for f in range(2)]
    lst5=[]
    lst5.append(df2.groupby('running').count().iloc[1]['x'])
    #lst5.append(df2.groupby('chasing').count().iloc[1]['x'])
    lst5.append(df2.groupby('climbing').count().iloc[1]['x'])
    lst5.append(df2.groupby('eating').count().iloc[1]['x'])
    lst5.append(df2.groupby('foraging').count().iloc[1]['x'])
    activity=['running','climbing', 'eating', 'foraging' ]
    lst6=[]
    lst6.append(df2.groupby('kuks').count().iloc[1]['x'])
    lst6.append(df2.groupby('quaas').count().iloc[1]['x'])
    lst6.append(df2.groupby('moans').count().iloc[1]['x'])
    calls=['kuks','quaas', 'moans']


    fig, axs = plt.subplots(2, 3, figsize=(30,15))
    fig.suptitle('SQUIRREL STATS', fontsize=50)
    matplotlib.pyplot.subplots_adjust(left=0.125, bottom=0.15, right=0.9, top=0.8, wspace=1.5, hspace=1.5)
    axs[0, 0].pie(sizes, explode=explode, labels=labels, radius=2, textprops={'fontsize': 30})
    axs[0, 0].set_title('COLOUR DISTRIBUTION', pad=70, fontsize=30)
    axs[0, 1].bar(x, height=lst, color=(0, 0.7, 0))
    axs[0, 1].set_title('VARIATION IN \n'+' SHIFT WISE SIGHTINGS', fontsize=30)
    axs[0, 1].set_xlabel('Shift', fontsize=25)
    axs[0, 1].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0, 1].tick_params(axis='both', which='major', labelsize=20)
    axs[1, 2].bar(lst3, height=lst2, color=(0.6, 0, 0))
    axs[1, 2].set_title('AGE DISTRIBUTION', fontsize=30)
    axs[1, 2].set_xlabel('Ages', fontsize=20)
    axs[1, 2].set_ylabel('Frequency of Ages', fontsize=25)
    axs[1, 0].bar(ground, height=lst4, color=(1, 0.8, 0.2))
    axs[1, 0].set_title('SQUIRREL LOCATIONS\n'+' OF SIGHTINGS', fontsize=30)
    axs[1, 0].set_xlabel('Locations', fontsize=25)
    axs[1, 0].set_ylabel('Frequency of Sightings', fontsize=25)
    axs[1, 0].tick_params(axis='both', which='major', labelsize=20)
    axs[1, 1].bar(activity, height=lst5)
    axs[1, 1].set_title('ACTIVITY\n'+' WISE SIGHTINGS', fontsize=30)
    axs[1, 1].tick_params(axis='x', rotation=90)
    axs[1, 1].set_xlabel('Activity', fontsize=25)
    axs[1, 1].set_ylabel('Frequency of sighting', fontsize=25)
    axs[1, 1].tick_params(axis='both', which='major', labelsize=20)
    axs[0, 2].bar(calls, height=lst6, color=(1, 0.6, 0))
    axs[0, 2].set_title('FREQUENCY\n'+' OF CALLS', fontsize=30)
    axs[0, 2].set_xlabel('Calls', fontsize=25)
    axs[0, 2].set_ylabel('Frequency of sightings', fontsize=25)
    axs[0, 2].tick_params(axis='both', which='major', labelsize=20)    


    buffer = BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    return HttpResponse(buffer.getvalue(), content_type="image/png")
# Create your views here.
