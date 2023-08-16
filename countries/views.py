from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    response=requests.get('https://restcountries.com/v3.1/all').json()
    countries_data = []
    for country_info in response:
        country_name = country_info['name']['common']
        currencies_info = country_info.get('currencies', {})
        currencies_names = ',\n'.join(currency_info['name'] for currency_info in currencies_info.values())

        countries = {
            "country": country_name,
            "currencies": currencies_names
        }
        countries_data.append(countries)
    print(countries_data)
    
    return render(request, 'countries/home.html', {'response':response})

