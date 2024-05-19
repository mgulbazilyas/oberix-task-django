from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name = 'index.html'


class Task1(TemplateView):
    template_name = 'task-1.html'


class Task2(TemplateView):
    template_name = 'task-2.html'


class Task3(TemplateView):
    template_name = 'index.html'


# Create your views here.

def mechanical(request, equipment, fault=0):

    return JsonResponse([
            {"Equipment": f"555CS-B-MECH-L02-FCU-E1/{equipment}-INT-E1", "Status": 1, "Fault": 0, "Fan Speed": "36%", "SA Temperature": "30.6°C", "Last Updated": "16/05/2024 01:53 PM"},
            {"Equipment": f"555CS-B-MECH-L02-FCU-E2/{equipment}-INT-E2", "Status": 1, "Fault": 0, "Fan Speed": "66%", "SA Temperature": "32.4°C", "Last Updated": "16/05/2024 01:54 PM"},
            {"Equipment": f"555CS-B-MECH-L02-FCU-E3/{equipment}-INT-E3", "Status": 1, "Fault": 0, "Fan Speed": "56%", "SA Temperature": "32.2°C", "Last Updated": "16/05/2024 01:54 PM"},
            {"Equipment": f"555CS-B-MECH-L02-FCU-N1/{equipment}-INT-N1", "Status": 1, "Fault": 0, "Fan Speed": "56%", "SA Temperature": "32.6°C", "Last Updated": "16/05/2024 01:54 PM"},
            {"Equipment": f"555CS-B-MECH-L02-FCU-N2/{equipment}-INT-N2", "Status": 1, "Fault": int(fault), "Fan Speed": "40%", "SA Temperature": "32.5°C", "Last Updated": "16/05/2024 01:56 PM"},
            {"Equipment": f"555CS-B-MECH-L02-FCU-N3/{equipment}-INT-N3", "Status": 1, "Fault": 0, "Fan Speed": "64%", "SA Temperature": "32.7°C", "Last Updated": "16/05/2024 01:57 PM"},
            {"Equipment": f"555CS-B-MECH-L02-FCU-W1/{equipment}-INT-W1", "Status": 0, "Fault": int(fault), "Fan Speed": "100%", "SA Temperature": "30.6°C", "Last Updated": "16/05/2024 01:54 PM"},
            {"Equipment": f"555CS-B-MECH-L02-FCU-W2/{equipment}-INT-W2", "Status": 1, "Fault": 0, "Fan Speed": "57%", "SA Temperature": "32.3°C", "Last Updated": "16/05/2024 01:56 PM"},
            {"Equipment": f"555CS-B-MECH-L03-FCU-E1/{equipment}-INT-E1", "Status": 1, "Fault": 0, "Fan Speed": "3%", "SA Temperature": "21°C", "Last Updated": "16/05/2024 01:56 PM"},
            {"Equipment": f"555CS-B-MECH-L03-FCU-E2/{equipment}-INT-E2", "Status": 1, "Fault": 0, "Fan Speed": "42%", "SA Temperature": "21.4°C", "Last Updated": "16/05/2024 01:59 PM"},
            {"Equipment": f"555CS-B-MECH-L03-FCU-N1/{equipment}-INT-N1", "Status": 1, "Fault": 0, "Fan Speed": "22%", "SA Temperature": "21.2°C", "Last Updated": "16/05/2024 01:59 PM"}
], safe=False
)

import random

def apiWeather(request, value):
    if value == 1:
        return JsonResponse({'Weather': 'Sunny', 'temperature': random.randint(100,10000)/100, 'image': '/static/icons/weather-sunny.svg'})
    elif value == 2:
        return JsonResponse({'Weather': 'Cloudy', 'temperature': random.randint(100,10000)/100, 'image': '/static/icons/weather-cloudy.svg'})
    elif value == 3:
        return JsonResponse({'Weather': 'Rain', 'temperature': random.randint(100,10000)/100, 'image': '/static/icons/weather-rain.svg'})
    else:
        return JsonResponse({'Weather': 'Unknown', 'temperature': random.randint(100,10000)/100})