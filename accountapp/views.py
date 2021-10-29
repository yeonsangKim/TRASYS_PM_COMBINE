from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

def main(request):
    return render(request, 'accountapp/main.html')

class accountcreateview(CreateView):      #기본적으로 제공해주는 틀
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:main')
    template_name = 'accountapp/create.html'







