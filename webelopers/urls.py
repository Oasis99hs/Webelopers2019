from django.urls import path
from .views import *

app_name = 'webelopers'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', register, name='register'),
    path('contact_us/', ContactView.as_view(), name='contact_us'),
    path('sent/', sent, name='sent'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profile/panel/', panel, name='panel'),
]
