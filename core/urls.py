from django.urls import path, include
from django.conf.urls import url, include
from .views import index
from .views import listarCategoria

urlpatterns = [
     path('', index, name=""),
     path('categorias', listarCategoria, name="categorias")
 ]
