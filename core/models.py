from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    rut = models.CharField(max_length=12)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField(default=0)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=14)
    altura = models.IntegerField(default=0)
    genero = models.CharField(max_length=10, choices=[('masculino','Masculino'),('femenino','Femenino')])
    habilitado = models.BooleanField(default=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    imagen = CloudinaryField('imagen')

    def __str__(self):
        return self.rut