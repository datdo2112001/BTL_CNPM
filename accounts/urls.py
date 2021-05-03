from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import UserRegisterView


urlpatterns = [
    path("register/", UserRegisterView.as_view(), name = 'register'),
]
