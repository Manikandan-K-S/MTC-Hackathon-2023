from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('random_challenge/', views.random_challenge, name='random_challenge'),
    path("carbon-footprints/",views.carbon_footprint,name='carbon-footprint'),
    path('carbon_car/', views.car_emission, name='carbon_car'),
    path('green-products/', views.green_products, name='green_products'),
    path('carbon_household/', views.household_emission, name='carbon_household'),
    path('donations/',views.donation,name='donations'),
    path('local-products/',views.products,name='products'),

    
]