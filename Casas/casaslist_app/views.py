#Concepto de serializacion y descerializacion de datos
# COMPLEX DATATYPE   --(Serialization)-->   PYTHON NATIVE DATATYPE  --(RENDER IN JSON)-->  JSON Data
# JSON DATA --(Parse data)-->   PYTHON NATIVE DATATYPE --(DE-SERIALIZATION)-->  COMPLEX DATATYPE


#from django.shortcuts import render
#from casaslist_app.models import Casa
#from django.http import JsonResponse
#
#
## Create your views here.
#
## Urls paso 4: crear la funcion, importar el modelo y crear las sentencias a ejecutar
#def casas_list(request):
#    casas = Casa.objects.all()
#    data = {
#        'casas': list(casas.values())
#    }
#    return JsonResponse(data)
#
#def casas_show(request, id):
#    casa = Casa.objects.get(pk = id)
#    data = {
#        'direccion': casa.direccion,
#        'pais': casa.pais,
#        'imagen': casa.imagen,
#        'active': casa.active,
#        'descripcion': casa.descripcion,
#    }
#    return JsonResponse(data)