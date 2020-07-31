import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    appid = '9fe9a3a4e1ef70f9102e15020f9ea57b'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    
    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    cities = City.objects.all()
    allcities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        cityinfo = {
            'city': city.name,
            'temperature': res["main"]["temp"],
            'icon': res['weather'][0]['icon']
        }
        allcities.append(cityinfo)

    context = {'all_info':allcities, 'form':form}

    return render(request, 'index.html', context)
