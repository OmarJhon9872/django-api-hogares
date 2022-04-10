from casaslist_app.api.serializers import CasaSerializer, EmpresaSerializer, ComentarioSerializer
from casaslist_app.models import Casa, Empresa, Comentario
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class ComentariosCreate(generics.CreateAPIView):
    serializer_class = ComentarioSerializer
    
    #Para devolver el comentario al cliente
    def get_queryset(self):
        return Comentario.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('id')
        casa = Casa.objects.get(pk = pk)
        
        user = self.request.user
        comentario_queryset = Comentario.objects.filter(casa = casa, comentario_user=user)
        
        if comentario_queryset.exists():
            raise ValidationError("No se puede agregar mas de un comentario a la casa por usuario")
        
        serializer.save(casa = casa, comentario_user=user)


#Clases genericas para el listado dinamico del serializer indicado y el queryset resultante
#la clase en automatico detectara que tipo de response crear de acuerdo a la instancia que herede la clase
class ComentariosList(generics.ListAPIView):
    #queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    #Sobreescribimos el metodo para indicar que el retrive podra ser generico de acuerdo a la
    #casa que se vaya a indicar como parametro
    def get_queryset(self):
        #Obtiene las propiedades que el cliente envia
        pk = self.kwargs['id']
        #Filtrara de acuerdo a la casa que sea indicada en la url como parametro
        return Comentario.objects.filter(casa = pk)

#Clase generica que podra consultar un dato, actualizar y eliminar un comentario
class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer





#Metodos genericos
#from rest_framework import mixins, generics
# class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer
#
#     #Propiedades del modelo y comentarios que vayan a generarse
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class ComentarioDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Comentario.objects.all()
#     serializer_class = ComentarioSerializer
#
#     def get(self, request, *args, **kwargs):
#         #Devolvera un comentario por el id
#         return self.retrieve(request, *args, **kwargs)






########################################################################
############ MODELO EMPRESA
########################################################################

#########################################################################
#Con la herencia de viewsets.ModelViewSet se define en automatico los verbos http get, post, put, delete
#########################################################################
class EmpresaVS(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


#########################################################################
#Con la definicion de APIView podemos definir segun el metodo HTTP recibido
#########################################################################
#from rest_framework.views import APIView
# class EmpresaAV(APIView):
#     def get(self, request):
#         empresas = Empresa.objects.all()
#         serializer = EmpresaSerializer(empresas, many = True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = EmpresaSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#########################################################################
#EMPLEAR VIEWSETS COMO UNA FORMA OPTIMA DE CREACION DE ENDPOINTS GENERICOS CON
#EL APOYO DE DEFAULTROUTER DE DJANGO (urls.py - router)
#from rest_framework import viewsets
#########################################################################
# class EmpresaVS(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Empresa.objects.all()
#         serializers = EmpresaSerializer(queryset, many=True)
#         return Response(serializers.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Empresa.objects.all()
#         casas_list = get_object_or_404(queryset, pk = pk)
#         serializer = EmpresaSerializer(casas_list)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = EmpresaSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk = pk)
#             serializer = EmpresaSerializer(empresa, request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Empresa.DoesNotExist:
#             return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
#
#     def destroy(self, request, pk):
#         try:
#             empresa = Empresa.objects.get(pk = pk)
#             empresa.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#
#         except Empresa.DoesNotExist:
#             return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)




#from rest_framework.views import APIView
class EmpresaDetalleAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk = pk)
            serializer = EmpresaSerializer(empresa, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk = pk)
            serializer = EmpresaSerializer(empresa, data = request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status = status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk = pk)
            empresa.delete()
            return Response(status = status.HTTP_204_NO_CONTENT)

        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)


########################################################################
############ MODELO CASA
########################################################################

########  Sustitucion de CasaListAV
# class CasaList2(generics.ListCreateAPIView):
#     serializer_class = CasaSerializer
#     queryset = Casa.objects.all()
#from rest_framework.views import APIView
#from rest_framework.response import Response
class CasaListAV(APIView):

    def get(self, request):
        casas = Casa.objects.all()
        serializer = CasaSerializer(casas, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CasaSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# class CasaShowAV2(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CasaSerializer
#     queryset = Casa.objects.all()
#     lookup_field = 'id'

#from rest_framework.views import APIView
class CasaShowAV(APIView):

    def get(self, request, id):
        try:
            casa = Casa.objects.get(pk = id)
        except Casa.DoesNotExist:
            return Response({'error': 'Casa no encontrada'}, status = status.HTTP_404_NOT_FOUND)

        serializer = CasaSerializer(casa)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            casa = Casa.objects.get(pk = id)
        except Casa.DoesNotExist:
            return Response({'error': 'Casa no encontrada'}, status = status.HTTP_404_NOT_FOUND)

        serializer = CasaSerializer(casa, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            casa = Casa.objects.get(pk = id)
        except Casa.DoesNotExist:
            return Response({'error': 'Casa no encontrada'}, status = status.HTTP_404_NOT_FOUND)

        casa.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
#from rest_framework.decorators import api_view
# @api_view(['GET', 'POST'])
# def casas_list(request):
#     if request.method == 'GET':
        
#         casas = Casa.objects.all()
#         #En caso de querer devolver varios elementos se indica un 2 parametro many=True
#         serializer = CasaSerializer(casas, many = True)
#         return Response(serializer.data)
        
        
#     elif request.method == 'POST':
#         #Deserializa la data que se va a recibir del request para crear un complex datatype
#         de_serializer = CasaSerializer(data = request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)
    
#from rest_framework.decorators import api_view
# @api_view(['GET', 'PUT', 'DELETE'])
# def casas_show(request, id):
    
#     if request.method == 'GET':
#         try:
#             casa = Casa.objects.get(pk = id)
#             serializer = CasaSerializer(casa)
#             return Response(serializer.data)
#         except Casa.DoesNotExist:
#             return Response({'error': 'Error, casa no encontrada'}, status = status.HTTP_404_NOT_FOUND)
        
#     elif request.method == 'PUT':
#         casa = Casa.objects.get(pk = id)
        
#         de_serializer = CasaSerializer(casa, data = request.data)
#         #Enviaremos un codigo de error 400 cuando el cliente envia data a procesar de forma erronea
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data) 
#         else:
#             return Response(de_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
#     elif request.method == 'DELETE':
#         try:
#             casa = Casa.objects.get(pk = id)
        
#             casa.delete()
#         except:
#             return Response({'error': "La casa que intentas eliminar no existe"}, status=status.HTTP_404_NOT_FOUND)
        
#         return Response(status = status.HTTP_204_NO_CONTENT)