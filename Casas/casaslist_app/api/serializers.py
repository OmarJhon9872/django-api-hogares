from rest_framework import serializers
from casaslist_app.models import Casa
#Para serializacion de datos se crearan los objetos encargados
#de mapear las instancias que definiran los tipos de datos

def longitud_columna(value):
    if len(value) < 2:
        raise serializers.ValidationError("El valor no debe ser de 2 caracteres solamente")


class CasaSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only = True)
    direccion = serializers.CharField( validators = [longitud_columna] )
    pais = serializers.CharField( validators = [longitud_columna] )
    descripcion = serializers.CharField()
    imagen = serializers.CharField(max_length = 10, error_messages={'max_length': 'El valor no debe ser de 10 caracteres solamente'})
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Casa.objects.create(**validated_data)
    
    def update(self, instanciaObjeto, validated_data):
        instanciaObjeto.direccion = validated_data.get('direccion', instanciaObjeto.direccion)
        instanciaObjeto.pais = validated_data.get('pais', instanciaObjeto.pais)
        instanciaObjeto.descripcion = validated_data.get('descripcion', instanciaObjeto.descripcion)
        instanciaObjeto.imagen = validated_data.get('imagen', instanciaObjeto.imagen)
        instanciaObjeto.active = validated_data.get('active', instanciaObjeto.active)
        
        instanciaObjeto.save()
        return instanciaObjeto
    #Funcion de Django predefinida para validaciones
    def validate(self, data):
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError("Pais y direccion iguales imposible")
        else:
            return data
        
    def validate_maxLength(self, data):
        if len(data) < 2:
            raise serializers.ValidationError("Url muy corto")
        else:
            return data