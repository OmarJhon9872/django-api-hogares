# Urls paso 2: importar y crear nuestros urlpatterns indicando como segundo
# parametro el nombre de la funcion que apuntara a los archivos de views.py(importar)


from django.urls import path
#from casaslist_app.api.views import casas_list, casas_show
from casaslist_app.api.views import CasaShowAV, CasaListAV

urlpatterns = [
    # Urls paso 3: ver archivo views.py
    path('list/', CasaListAV.as_view(), name='casas_list'),
    path('<int:id>', CasaShowAV.as_view(),  name='casas_show'),
]

