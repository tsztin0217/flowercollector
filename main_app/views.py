# main_app/views.py

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Flower, Pot
from .forms import WateringForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def about(request):
    return render(request, 'about.html')


class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('flower-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )


@login_required
def flower_index(request):
    flowers = Flower.objects.filter(user=request.user)
    return render(request, 'flowers/index.html', {'flowers': flowers})

@login_required
def flower_detail(request, flower_id):
    flower = Flower.objects.get(id=flower_id)
    pots_flower_doesnt_have = Flower.objects.exclude(id__in = flower.pots.all().values_list('id'))
    watering_form = WateringForm()

    return render(request, 'flowers/detail.html', {
        'flower': flower,
        'watering_form': watering_form,
        'pots': pots_flower_doesnt_have
    })


class FlowerCreate(LoginRequiredMixin, CreateView):
    model = Flower
    fields = ['name', 'color']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class FlowerUpdate(LoginRequiredMixin, UpdateView):
    model = Flower
    fields = ['color']


class FlowerDelete(LoginRequiredMixin, DeleteView):
    model = Flower
    success_url = '/flowers/'

@login_required
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


class PotCreate(LoginRequiredMixin, CreateView):
    model = Pot
    fields = '__all__'


class PotList(LoginRequiredMixin, ListView):
    model = Pot


class PotDetail(LoginRequiredMixin, DetailView):
    model = Pot


class PotUpdate(LoginRequiredMixin, UpdateView):
    model = Pot
    fields = ['name', 'color']


class PotDelete(LoginRequiredMixin, DeleteView):
    model = Pot
    success_url = '/pots/'


@login_required
def associate_pot(request, flower_id, pot_id):
    Flower.objects.get(id=flower_id).pots.add(pot_id)
    return redirect('flower-detail', flower_id=flower_id)

@login_required
def remove_pot(request, flower_id, pot_id):
    Flower.objects.get(id=flower_id).pots.remove(pot_id)
    return redirect('flower-detail', flower_id=flower_id)

