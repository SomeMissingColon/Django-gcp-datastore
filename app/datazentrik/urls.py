"""
URL Mappings
"""

from django.urls import path

from datazentrik import views

app_name ='datazentrik'

urlpatterns = [
    path('', views.landing, name='landing'),
]