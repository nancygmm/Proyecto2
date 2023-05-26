from distutils.sysconfig import customize_compiler
from django.urls import path


from . import views
from django.urls import path, include
from django.contrib import admin
from . import views as core_views
from .views import SignUpView




urlpatterns = [
    path('', views.store),
    path('store/', views.store),
    path('resultado/', views.resultado, name='resultado'),


    path("accounts/", include("django.contrib.auth.urls")),
]