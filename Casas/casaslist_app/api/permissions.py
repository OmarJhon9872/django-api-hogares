from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        #Si el metodo es GET sera un metodo de listado de recursos o read_only
        if request.method == 'GET':
            return True
        
        #El permiso staff indica que el usuario tiene autorizacion de modificar recursos del sistema
        permiso_staff = bool(request.user and request.user.is_staff)
        return permiso_staff
    
class ComentarioUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Representacion de metodos get unicamente, read_only
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.comentario_user == request.user
            