from django.shortcuts import render
from django.urls import reverse_lazy
from .models import CustomUser
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'home.html')

class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
