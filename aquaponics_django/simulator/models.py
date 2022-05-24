from django.db import models

# Create your models here.
class Cultivo(models.Model):
  """ Modelo de los cultivos con información de 
  tipo, temperaturas y germinación
  """

  cultivo = models.CharField(max_length=70,help_text="El nombre del cultivo.")
  tipo = models.CharField(max_length=30,help_text="El tipo de cultivo.")
  t_min = models.FloatField(max_length=10,verbose_name="La temperatura minima del cultivo.")
  t_max = models.FloatField(max_length=10,verbose_name="La temperatura maxima del cultivo.")
  t_opt = models.FloatField(max_length=10,verbose_name="La temperatura optima del cultivo.")
  germinacion_1 = models.IntegerField(verbose_name="Tiempo en dias de primera cosecha.")
  germinacion_n = models.IntegerField(verbose_name="Tiempo en dias entre cosechas.")
  distancia = models.FloatField(max_length=10,help_text="Separacion entre plantas del cultvo.")
  primera_cosecha = models.FloatField(max_length=10,help_text="Numero de meses para la primera cosecha.")
  n_cosechas = models.FloatField(max_length=10,help_text="Numero de cosechas al año.")
  distanciaXcosechaAnual = models.FloatField(max_length=10, verbose_name="Distancia por cosecha anual.")
  municipios = models.ManyToManyField('Municipio',through='MunicipiosCultivo')

  def __str__(self) -> str:
    return self.cultivo

class Municipio(models.Model):
  municipio = models.CharField(max_length=70,help_text="El nombre del municipio")
  departamento = models.CharField(max_length=70,help_text="Nombre del departamento del municipio.")
  t_min = models.FloatField(max_length=30,help_text="Temperatura minima del municipio.")
  t_avg = models.FloatField(max_length=30,help_text="Temperatura promedio del municipio.")
  t_max = models.FloatField(max_length=30,help_text="Temperatura maxima del municipio.")
  
class MunicipiosCultivo(models.Model):
  cultivo = models.ForeignKey(Cultivo,on_delete=models.CASCADE)
  municipio = models.ForeignKey(Municipio,on_delete=models.CASCADE)

