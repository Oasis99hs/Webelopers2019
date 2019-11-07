from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import *


# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'


class RegisterView(generic.TemplateView):
    template_name = 'register.html'


def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    user = User(first_name, last_name, username, email, password1)
    print(first_name)
    print(last_name)
    print(username)
    print(email)
    print(password1)
    user.save()
    return HttpResponseRedirect(reverse('webelopers:register'))
