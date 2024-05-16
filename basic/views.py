from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

class Homepage(TemplateView):
    template_name = 'index.html'


# Create your views here.

def mechanical(request, equipment):

    return JsonResponse([
    {"Equipment":f"{equipment}-L01-01", "Status":1, "Fault":0},
    {"Equipment":f"{equipment}-L01-02", "Status":1, "Fault":0},
    {"Equipment":f"{equipment}-L01-03", "Status":1, "Fault":0},
    {"Equipment":f"{equipment}-L01-04", "Status":0, "Fault":1},
    {"Equipment":f"{equipment}-L01-05", "Status":1, "Fault":0},
    {"Equipment":f"{equipment}-L01-06", "Status":0, "Fault":0},
    {"Equipment":f"{equipment}-L01-07", "Status":1, "Fault":0}
], safe=False
)