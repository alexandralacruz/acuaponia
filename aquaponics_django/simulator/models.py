from django.db import models

# Create your models here.
class Simulator(models.Model):
  name = models.CharField(max_length=255)
  slug = models.SlugField

  class Meta:
    ordering = ('name',)

  def __str__(self) -> str:
    return self.name
  
  def get_message(self):
    return "Hell from Django"