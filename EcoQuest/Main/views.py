from django.http import JsonResponse
from django.shortcuts import render
import random
from .challenges import challenges_data

def index(request):
    return render(request,'index.html')

def green_products(request):
    return render(request, 'green_products.html')

def random_challenge(request):
    challenges_list = challenges_data["challenges"][:5]
    random_challenge = random.choice(challenges_list)
    
    context = {
        "challenge": random_challenge
    }
    
    return render(request, "challenge_page.html", context)



def carbon_footprint(request):
    return render(request, 'carbon_footprint.html')


def carbon_car(car_mileage, miles_driven): 
    emission_factor = 19.6  
    footprint_car = (miles_driven / car_mileage) * emission_factor
    return footprint_car


def carbon_household(electricity_consumption):
    emission_factor = 0.92
    footprint_household = electricity_consumption * emission_factor
    return footprint_household



def car_emission(request):
    if request.method == 'POST':
        miles_driven = float(request.POST.get('miles_driven', 0))
        carbon_emission = carbon_car(miles_driven)
        return JsonResponse({'carbon_emission': carbon_emission})
    return render(request, 'car_emission.html')

def household_emission(request):
    if request.method == 'POST':
        print(1)
        electricity_consumption = float(request.POST.get('electricity_consumption', 0))
        print(2)
        carbon_emission = carbon_household(electricity_consumption)
        return JsonResponse({'carbon_emission': carbon_emission})
    return render(request, 'household_emission.html')

def donation(request):
    return render(request, 'donations.html')
def products(request):
    pass