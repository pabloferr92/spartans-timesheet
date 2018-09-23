from django.shortcuts import render
from .models.usuarios import Users

# Create your views here.
def index(request):
    return render(request, "index.html")

def listaUsuarios(request):
    return render(request,'usuarios.html',{'usuarios': Users.objects.all()})