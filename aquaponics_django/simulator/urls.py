from django.contrib import admin
from django.urls import path, include
from simulator import views

urlpatterns = [
  path('datos-hidroponia/',views.DatosHidroponia.as_view()),
  path('datos-municipios/',views.DatosMunicipios.as_view()),
]