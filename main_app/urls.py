from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('flowers/', views.flower_index, name='flower-index'),
    path('flowers/<int:flower_id>/', views.flower_detail, name='flower-detail'),
]
