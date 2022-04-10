from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length = 255)
    website = models.URLField(max_length = 255)
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
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='casas_list', default=None)
    #Campo que va a desplegar en el django administration, indice que represente a cada elemento
    def __str__(self):
        return self.descripcion


class Comentario(models.Model):
    comentario_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    calificacion = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=250, null=True)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='comentarios')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.calificacion) + " " + self.casa.direccion