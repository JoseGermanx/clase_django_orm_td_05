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

class Pedido(models.Model):
    producto = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos_rel')

    def __str__(self):
        return f"{self.producto} - {self.total}"