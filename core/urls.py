from django.urls import path, include
from django.conf.urls import url, include
from .views import index
urlpatterns = [
     path('', index, name=""),
 ]
