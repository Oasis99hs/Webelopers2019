from django.urls import path
from .views import *

app_name = 'webelopers'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('registered/', register, name='registered'),
    path('contact_us/', ContactView.as_view(), name='contact_us'),
    path('sent/', sent, name='sent'),
    path('login/', login_user, name='login'),
]
