from django.shortcuts import render
from django.urls import path, include

from simulator import views
from .models import Cultivo,Municipio,MunicipiosCultivo
from .serializers import CultivoSerializer, MunicipiosSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class DatosHidroponia(APIView):
  def get(self,request,format=None):
    cultivos = Cultivo.objects.all()
    serializer = CultivoSerializer(cultivos,many=True)
    return Response(serializer.data)

class DatosMunicipios(APIView):
  def get(self,request,format=None):
    municipios = Municipio.objects.all()
    serializer = MunicipiosSerializer(municipios,many=True)
    return Response(serializer.data)