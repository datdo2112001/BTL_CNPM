from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')
