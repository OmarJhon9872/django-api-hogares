from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_view, logout_view

urlpatterns = [
    #Path definido por rest que permite la obtencion de un token 
    path('login/', obtain_auth_token, name='login'),

    #Path que va a emplear la funcion que creamos junto con el serializer
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
]