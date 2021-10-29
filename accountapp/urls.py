from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create, name='create'),
    path('location/', views.location, name='location'),
    path('data/', views.data, name='data')
]