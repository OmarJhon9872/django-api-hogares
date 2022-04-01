from rest_framework import serializers
from casaslist_app.models import Casa
from casaslist_app.models import Comentario
from casaslist_app.models import Empresa
#Para serializacion de datos se crearan los objetos encargados
#de mapear las instancias que definiran los tipos de datos

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        #fields = '__all__'
        exclude = ['casa']

class CasaSerializer(serializers.ModelSerializer):

    comentarios = ComentarioSerializer(many=True, read_only=True)
    #Campos calculados
    #longitud_direccion = serializers.SerializerMethodField()

    #Funcion que mapea los campos de mi modelo como en la primer definicion planteada abajo
    class Meta:
        model = Casa
        fields = "__all__"
        #fields = ['id', 'active']
        #exclude = ['id']


#class EmpresaSerializer(serializers.ModelSerializer):
class EmpresaSerializer(serializers.ModelSerializer):
    casas_list = CasaSerializer(many=True, read_only=True)

    class Meta:
        model = Empresa
        fields = '__all__'



    #StringRelatedField Este metodo indica el retorno de la definicion __str__ del modelo serializado
    #casas_list = serializers.StringRelatedField(many=True)
    #casas_list = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # casas_list = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name = 'casas-detail',
    #     required=False,
    #     lookup_field='id'
    # )
        
    # def get_longitud_direccion(self, object):
    #     cantidad_caracteres = len(object.direccion)
    #     return cantidad_caracteres
    #
    # #Funciones a nivel de CasaSerializer
    # def validate(self, data):
    #     if data['direccion'] == data['pais']:
    #         raise serializers.ValidationError("Pais y direccion iguales imposible")
    #     else:
    #         return data
    #
    # def validate_maxLength(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError("Url muy corto")
    #     else:
    #         return data


#############################################################################
#######       Primer definicion de toda la logica del sistema

# def longitud_columna(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("El valor no debe ser de 2 caracteres solamente")

# class CasaSerializer(serializers.Serializer):
    
#     id = serializers.IntegerField(read_only = True)
#     direccion = serializers.CharField( validators = [longitud_columna] )
#     pais = serializers.CharField( validators = [longitud_columna] )
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField(max_length = 10, error_messages={'max_length': 'El valor no debe ser de 10 caracteres solamente'})
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Casa.objects.create(**validated_data)
    
#     def update(self, instanciaObjeto, validated_data):
#         instanciaObjeto.direccion = validated_data.get('direccion', instanciaObjeto.direccion)
#         instanciaObjeto.pais = validated_data.get('pais', instanciaObjeto.pais)
#         instanciaObjeto.descripcion = validated_data.get('descripcion', instanciaObjeto.descripcion)
#         instanciaObjeto.imagen = validated_data.get('imagen', instanciaObjeto.imagen)
#         instanciaObjeto.active = validated_data.get('active', instanciaObjeto.active)
        
#         instanciaObjeto.save()
#         return instanciaObjeto
#     #Funcion de Django predefinida para validaciones
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError("Pais y direccion iguales imposible")
#         else:
#             return data
        
#     def validate_maxLength(self, data):
#         if len(data) < 2:
#             raise serializers.ValidationError("Url muy corto")
#         else:
#             return data