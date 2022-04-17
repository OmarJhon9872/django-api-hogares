from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #Path definido por rest que permite la obtencion de un token 
    path('login/', obtain_auth_token, name='login'),
]