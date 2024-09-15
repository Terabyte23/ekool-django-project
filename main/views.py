from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy


def index(request):
    return render(request, 'main/login.html')


def sisine(request):
    return render(request, 'main/sisine.html')


def menu(request):
    return render(request, 'main/menu.html')


def profil(request):
    return render(request, 'main/profil.html')


def ulesaned(request):
    return render(request, 'main/ulesaned.html')


class HomeView(TemplateView):
    template_name: str = 'main/login.html'
    template_name = 'main/login.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('index')
    template_name = 'main/sisine.html'
