from django.urls import path

from locationapp.views import main, showmap

app_name= 'locationapp'

urlpatterns = [
    path('main', main, name='main'),      #showmap,/<int:pk>
    path('json_data/', showmap, name='showmap')
]