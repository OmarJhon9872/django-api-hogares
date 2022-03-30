from casaslist_app.api.serializers import CasaSerializer
from casaslist_app.models import Casa
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

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
        