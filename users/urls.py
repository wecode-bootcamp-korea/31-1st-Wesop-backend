from django.urls import path
from .views import *

urlpatterns = [
    path('/check', check_email),
    path('/signup', sign_up),
    path('/login', log_in)
]