"""
URL Mappings for bouncer.
"""
from django.urls import path

from datazentrik import views


app_name = 'datazentrik'


urlpatterns = [
    path('<str:slug>/', views.handle_redirect, name='redirect'),
    path('', views.landing, name='landing'),
]