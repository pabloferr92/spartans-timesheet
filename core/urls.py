from django.urls import path, include
from django.conf.urls import url, include
from .views import index, listaUsuarios
urlpatterns = [
     path('', index, name=""),
     path('listausuarios/', listaUsuarios, name='listausuarios')
 ]