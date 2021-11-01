from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def data_usage(request):
    return render(request, 'usageapp/data_usage.html')