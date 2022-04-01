# Urls paso 2: importar y crear nuestros urlpatterns indicando como segundo
# parametro el nombre de la funcion que apuntara a los archivos de views.py(importar)


from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from casaslist_app.api.views import casas_list, casas_show
from casaslist_app.api.views import (CasaShowAV, CasaListAV,
                                     ComentariosList,ComentarioDetail, ComentariosCreate, EmpresaVS)

#Luego en EmpresaSerializer se remplaza de HyperlinkedModelSerializer a ModelSerializer
router = DefaultRouter()
router.register('empresa', EmpresaVS, basename='empresa')

# Urls paso 3: ver archivo views.py
urlpatterns = [
    path('casa/', CasaListAV.as_view(), name='casas'),
    path('casa/<int:id>', CasaShowAV.as_view(),  name='casas-detail'),

    path('', include(router.urls)),
    #from casaslist_app.api.views import EmpresaAV, EmpresaDetalleAV (APIViews)
    # path('empresa/', EmpresaAV.as_view(), name='empresa'),
    # path('empresa/<int:pk>', EmpresaDetalleAV.as_view(),  name='empresa-detail'),

    path('casa/<int:id>/comentario-create', ComentariosCreate.as_view(), name='comentario-create'),
    path('casa/<int:id>/comentario/', ComentariosList.as_view(), name='comentario-list'),
    path('casa/comentario/<int:pk>', ComentarioDetail.as_view(),  name='comentario-detail')
]