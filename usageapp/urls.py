from django.urls import path

from usageapp.views import data_usage, chart

app_name = 'usageapp'

urlpatterns = [
    path('data_usage/', data_usage, name='data_usage'),
    path('json_chart/', chart, name='chart')
]