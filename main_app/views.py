from django.shortcuts import render
from django.db import models
from .models import Flower

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
    return render(request, 'flowers/detail.html', {'flower': flower})