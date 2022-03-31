from django.contrib import admin

# Models paso 2, importar la definicion del modelo, buscar linea admin.site.register(Casa)
from casaslist_app.models import Casa, Empresa
# Register your models here.

# Models paso 3, Se registra en la app, luego se crea la instancia para generar sql
# python3 manage.py makemigrations
# y finalmente se cargan los cambios con
# python3 manage.py migrate
admin.site.register(Casa)
admin.site.register(Empresa)