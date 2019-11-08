from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'index.html'


def register(request):
    if not request.POST:
        return render(request, 'register.html')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    context = {}
    users = User.objects.filter(username=username)
    valid = True
    if users:
        context['username_invalid'] = True
        valid = False
    if password1 != password2:
        context['password_invalid'] = True
        valid = False
    if valid:
        user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
        user.set_password(password1)
        user.save()
        return redirect('webelopers:register')
    else:
        return render(request, 'register.html', context)


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


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='../login/')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='../login/')
def edit_profile(request):
    if not request.POST:
        return render(request, 'edit_profile.html')
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    user = User.objects.get(username=request.user.username)
    if first_name != '':
        user.first_name = first_name
    if last_name != '':
        user.last_name = last_name
    user.save()
    return redirect('webelopers:profile')
