
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import create, login, logout

app_name = "accountapp"

urlpatterns = [
    path('create/', create, name='create'),
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
]