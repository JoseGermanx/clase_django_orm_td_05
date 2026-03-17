from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    activo = models.BooleanField(default=True)
    visitas = models.IntegerField(default=0)
    pedidos = models.IntegerField(default=0)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    