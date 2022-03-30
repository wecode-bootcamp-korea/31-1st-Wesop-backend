from django.urls import path
from .views import *

urlpatterns = [
    path('/check', CheckEmail),
    path('/signup', SignUp),
    path('/login', Login)
]