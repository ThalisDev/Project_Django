
from django.urls import path
from .views import Home, addUser
from . import views

urlpatterns = [
    path('',Home, name='Home'),#pagina index
    path('addUser',addUser,name='addUser'),#função grava no banco de dados
]
