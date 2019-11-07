from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic


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
    return render(request, 'sent.html')
