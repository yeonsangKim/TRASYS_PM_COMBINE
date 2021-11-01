from django.urls import path

from locationapp.views import main

app_name= 'locationapp'

urlpatterns = [
    path('main/', main, name='main')
]