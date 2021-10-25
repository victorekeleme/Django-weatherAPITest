from django.shortcuts import render, redirect
import urllib.request
import json

# Create your views here.

#api display view
def api_display(request):
    #api key
    APIkey = '9d50450a48809637b4862bdcb125927d'

    if request.method == 'POST': #if post method
        # initial a variable to hold the value of city
        city = request.POST['btn'].lower()
        #if statement to get corresponding city_id and language
        if city == 'london':
            city_id = 2643743
            lang = 'en'
        elif city == 'paris':
            city_id = 2988507
            lang = 'fr'
        elif city == 'new york':
            city_id = 5128581
            lang = 'en'
        elif city == 'delhi':
            city_id = 2650225
            lang = 'hi'
        elif city == 'tokyo':
            city_id = 1850147
            lang = 'ja'
        else:
            city_id = None

        #api request source
        source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&lang={lang}&appid={APIkey}').read()

        #Json data for the requested city
        list_of_data = json.loads(source)

        #selected city data to be consumed
        data = {
            "city_name": str(city),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "humidity": str(list_of_data['main']['humidity']),
            "description": str(list_of_data['weather'][0]['description']),
            "temp_min": str(list_of_data['main']['temp_min']) + '°C',
            "temp_max": str(list_of_data['main']['temp_max']) + '°C',

        }
    else:
        #if not post method initialize empty data dictionary
        data = {}

    return render(request, 'weatherapi/index.html', data) # returns the data to the frontend
