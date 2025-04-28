from django.shortcuts import render, redirect
from .models import Flower, Pot
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WateringForm
from django.views.generic import ListView, DetailView

def about(request):
    return render(request, 'about.html')


# class Flower:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# # Create a list of Flower instances
# flowers = [
#     Flower('Rose', 'red'),
#     Flower('Lily', 'yellow'),
#     Flower('Poppy', 'red'),
#     Flower('Orchid', 'purple')
# ]

def home(request):
    return render(request, 'home.html')

def flower_index(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers/index.html', {'flowers': flowers})

def flower_detail(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    pots_flower_doesnt_have = Flower.objects.exclude(id__in = flower.pots.all().values_list('id'))
    watering_form = WateringForm()

    return render(request, 'flowers/detail.html', {
        'flower': flower,
        'watering_form': watering_form,
        'pots': pots_flower_doesnt_have
    })


class FlowerCreate(CreateView):
    model = Flower
    fields = ['name', 'color']

class FlowerUpdate(UpdateView):
    model = Flower
    fields = ['color']

class FlowerDelete(DeleteView):
    model = Flower
    success_url = '/flowers/'

def add_watering(request, flower_id):
    # create a ModelForm instance using the data in request.POST
    form = WateringForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the flower_id assigned
        new_watering = form.save(commit=False)
        new_watering.flower_id = flower_id
        new_watering.save()
    return redirect('flower-detail', flower_id=flower_id)

class PotCreate(CreateView):
    model = Pot
    fields = '__all__'

class PotList(ListView):
    model = Pot

class PotDetail(DetailView):
    model = Pot

class PotUpdate(UpdateView):
    model = Pot
    fields = ['name', 'color']

class PotDelete(DeleteView):
    model = Pot
    success_url = '/pots/'



def associate_pot(request, flower_id, pot_id):
    Flower.objects.get(id=flower_id).pots.add(pot_id)
    return redirect('flower-detail', flower_id=flower_id)


def remove_pot(request, flower_id, pot_id):
    Flower.objects.get(id=flower_id).pots.remove(pot_id)
    return redirect('flower-detail', flower_id=flower_id)