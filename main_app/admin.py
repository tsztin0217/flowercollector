from django.contrib import admin
from .models import Flower, Watering, Pot

# Register your models here.
admin.site.register([Flower, Watering, Pot])