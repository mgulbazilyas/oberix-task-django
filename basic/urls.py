from django.contrib import admin
from django.urls import path
from basic import views
appname = 'basic'

urlpatterns = [
    path('', views.Homepage.as_view(), name='home'),
    path('mechanical/<str:equipment>/', views.mechanical, name='mechanical'),
]
