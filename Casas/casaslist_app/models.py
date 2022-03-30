from django.db import models

# Create your models here.

# Models paso 1 Para crear modelos primero se definen, luego en la app en admin.py se registran...
class Casa(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    imagen = models.TextField()
    active = models.BooleanField(default=True)
    #Campo que va a desplegar en el django administration, indice que represente a cada elemento
    def __str__(self):
        return self.descripcion