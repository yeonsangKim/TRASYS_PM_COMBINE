from django.urls import path
from . import views
from .views import accountcreateview

app_name = "accountapp"

urlpatterns = [
    path('', views.main, name='main'),

    path('create/', accountcreateview.as_view(), name='create')

]