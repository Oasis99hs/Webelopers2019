from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login


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
    user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
    user.set_password(password1)
    user.save()
    return HttpResponseRedirect(reverse('webelopers:register'))


class ContactView(generic.TemplateView):
    template_name = 'contact_us.html'


def sent(request):
    title = request.POST['title']
    email = request.POST['email']
    text = request.POST['text']
    if 250 > len(text) >= 10:
        return render(request, 'sent.html')
    else:
        return redirect('webelopers:contact_us')


def login_user(request):
    if not request.POST:
        return render(request, 'login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    else:
        return render(request, "login.html", {"error": True})
