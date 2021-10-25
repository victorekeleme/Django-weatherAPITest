from django.shortcuts import render, redirect
import urllib.request
import json



def api_display_test_data(city):

    APIkey = '9d50450a48809637b4862bdcb125927d'

    city_name = city.lower()
    if city_name == 'london':
        city_id = 2643743
        lang = 'en'
    elif city_name == 'paris':
        city_id = 2988507
        lang = 'fr'
    elif city_name == 'new york':
        city_id = 5128581
        lang = 'en'
    elif city_name == 'delhi':
        city_id = 2650225
        lang = 'hi'
    elif city_name == 'tokyo':
        city_id = 1850147
        lang = 'ja'
    else:
        city_id = None

    source = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&lang={lang}&appid={APIkey}').read()

    list_of_data = json.loads(source)

    data = {
        "city_name": str(city),
        "temp": str(list_of_data['main']['temp']) + '°C',
        "humidity": str(list_of_data['main']['humidity']),
        "description": str(list_of_data['weather'][0]['description']),
        "temp_min": str(list_of_data['main']['temp_min']) + '°C',
        "temp_max": str(list_of_data['main']['temp_max']) + '°C',

    }

    return data