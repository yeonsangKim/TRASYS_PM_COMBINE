from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from locationapp.models import Parking
from locationapp.serializers import pm_combine


@login_required
def data_usage(request):
    return render(request, 'usageapp/data_usage.html')

@api_view(["GET"])
def chart(request):       #,pk
    location = Parking.objects.all()

    temp = pm_combine(location, many=True)

    return Response(temp.data)