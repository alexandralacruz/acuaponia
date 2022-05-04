from django.contrib import admin
from django.urls import path, include
from simulator import views

urlpatterns = [
  path('simulator/',views.Simulator.as_view()),
]