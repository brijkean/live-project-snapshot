from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StationForm
from .models import Station


# Function that renders the home page
def radioHome(request):
    return render(request, 'CommunityFM/fm_home.html')

#Function to add a new station to the database
def add_station(request):
    form = StationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('addStation')
    else:
        print(form.errors)
        form = StationForm()
    return render(request, "CommunityFM/fm_create.html", {"form": form})

def station_index(request):
    stations = Station.objects.all()
    return render(request, 'CommunityFM/fm_index.html', {'stations': stations})

def station_details(request, pk):
    pk = int(pk)
    station = get_object_or_404(Station, pk=pk)
    context = {'station': station}
    return render(request, 'CommunityFM/fm_details.html', context)

def station_edit(request, pk):
    pk = int(pk)
    station = get_object_or_404(Station, pk=pk)
    form = StationForm(data=request.POST or None, instance=station)
    if request.method == 'POST':
        if form.is_valid():
            station = form.save(commit=False)
            station.save()
            return redirect('details', pk=station.pk)
        else:
            print(form.errors)
    else:
        return render(request, 'CommunityFM/fm_edit.html', {'form': form})


def station_delete(request, pk):
    pk = int(pk)
    station = get_object_or_404(Station, pk=pk)
    if request.method == 'POST':
        station.delete()
        return redirect('index')
    return render(request, "CommunityFM/fm_delete.html", {"station": station})



