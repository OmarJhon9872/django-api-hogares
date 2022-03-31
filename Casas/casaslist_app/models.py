from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length = 255)
    sitioWeb = models.URLField(max_length = 255)
    activo = models.BooleanField(max_length = 255)

    def __str__(self):
        return self.nombre


# Models paso 1 Para crear modelos primero se definen, luego en la app en admin.py se registran...
class Casa(models.Model):
    direccion = models.CharField(max_length = 250)
    pais = models.CharField(max_length = 250)
    descripcion = models.CharField(max_length = 250)
    imagen = models.TextField()
    active = models.BooleanField(default = True)
    create = models.DateTimeField(auto_now_add = True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='empresa_id', default=None)
    #Campo que va a desplegar en el django administration, indice que represente a cada elemento
    def __str__(self):
        return self.descripcion