import imp
from django.shortcuts import render
from django.urls import path, include

from simulator import views
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class Simulator(APIView):
  def get(self,request,format=None):
    return Response('Simulador de acuapónicos usando Django')