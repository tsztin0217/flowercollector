from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('flowers/', views.flower_index, name='flower-index'),
    path('flowers/<int:flower_id>/', views.flower_detail, name='flower-detail'),
    path('flowers/create/', views.FlowerCreate.as_view(), name='flower-create'),
    path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flower-update'),
    path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flower-delete'),
    path(
        'flowers/<int:flower_id>/add-watering/', 
        views.add_watering, 
        name='add-watering'
    ),
    path('pots/create/', views.PotCreate.as_view(), name='pot-create'),
    path('pots/<int:pk>/', views.PotDetail.as_view(), name='pot-detail'),
    path('pots/', views.PotList.as_view(), name='pot-index'),
    path('pots/<int:pk>/update/', views.PotUpdate.as_view(), name='pot-update'),
    path('pots/<int:pk>/delete/', views.PotDelete.as_view(), name='pot-delete'),
    path('flowers/<int:flower_id>/associate-pot/<int:pot_id>/', views.associate_pot, name='associate-pot'),
    path('flowers/<int:flower_id>/remove-pot/<int:pot_id>/', views.remove_pot, name='remove-pot'),
    path('accounts/signup/', views.signup, name='signup'),
]
