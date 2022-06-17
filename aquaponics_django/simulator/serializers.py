from rest_framework import serializers

from .models import Cultivo, Municipio, MunicipiosCultivo

class CultivoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cultivo
    fields = (
      'cultivo',
      'tipo',
      't_min',
      't_max',
      't_opt',
      'germinacion_1',
      'germinacion_n',
      'distancia',
      'primera_cosecha',
      'n_cosechas',
      'distanciaXcosechaAnual',
      'municipios'
    )

class MunicipiosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Municipio
    fields = (
      'municipio',
      'departamento',
      't_min',
      't_avg',
      't_max',
    )