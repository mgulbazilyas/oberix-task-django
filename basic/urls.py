from django.contrib import admin
from django.urls import path
from basic import views

app_name = 'basic'

urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('task-1/', views.Task1.as_view(), name='task-1'),
    path('task-2/', views.Task2.as_view(), name='task-2'),
    path('task-3/', views.Task3.as_view(), name='task-3'),
    path('api/weather/<int:value>/', views.apiWeather, name='api-weather'),
    path('mechanical/<str:equipment>/', views.mechanical, name='mechanical'),
    path('mechanical/<str:equipment>/<int:fault>/', views.mechanical, name='mechanical-fault'),
]