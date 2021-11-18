import self as self
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import  json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

from locationapp.models import Parking
from locationapp.serializers import pm_combine


@login_required
def main(request):
    return render(request, 'locationapp/main.html')

@api_view(["GET"])
def showmap(request):       #,pk
    location = Parking.objects.all()

    temp = pm_combine(location, many=True)

    return Response(temp.data)
