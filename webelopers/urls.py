from django.urls import path
from .views import *

app_name = 'webelopers'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('registered/', register, name='registered'),
]
