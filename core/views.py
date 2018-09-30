from django.shortcuts import render
from .models.categoria import Categoria

# Create your views here.
def index(request):
    return render(request, "index.html")


def listarCategoria(request):
    return render(request, 'categorias.html', {'categorias': Categoria.objects.all()})

def inserirProfessor(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        email=request.POST.get("email")
        logon=request.POST.get("logon")
        try:
            professor = Professor.objects.get(email=email)
            context = {
                "mensagem": "Email já cadastrado em Professores",
                "statusCode": "500",
                "cor": "red"
            }
            return render(request, "formNovoProfessor.html", context)
        except:
            try:
                professor = Professor.objects.get(logon=logon)
                context = {
                    "mensagem": "Logon já cadastrado em Professores",
                    "statusCode": "500",
                    "cor": "red"
                }
                return render(request, "formNovoProfessor.html", context)
            except:
                try:
                    professor=Aluno.objects.get(logon=logon)
                    context = {
                        "mensagem" : "Logon já cadastrado em Alunos",
                        "statusCode": "500",
                        "cor": "red"
                    }
                    return render(request, "formNovoProfessor.html", context)
                except:
                    Professor.objects.create (
                        logon = request.POST.get('logon'),
                        senha = request.POST.get('senha'),
                        nome = request.POST.get('nome'),
                        email = request.POST.get('email'),
                        celular = request.POST.get('celular'),
                        dtexpiracao = request.POST.get('dtexpiracao'),
                        apelido = request.POST.get('apelido')
                    )
                    return redirect('listarprofessores')
    else:
        return render(request, 'formNovoProfessor.html')

def alterarProfessor(request, idprofessor):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    professor = Professor.objects.get(idprofessor=idprofessor)
    if request.method == 'POST':
       professores = Professor.objects.get(idprofessor=idprofessor)
       professores.logon = request.POST.get('logon')
       professores.senha = request.POST.get('senha')
       professores.nome = request.POST.get('nome')
       professores.email = request.POST.get('email')
       professores.celular = request.POST.get('celular')
       professores.dtExpiracao = request.POST.get('dtexpiracao')
       professores.apelido = request.POST.get('apelido')
       professores.save()
       return redirect('listarprofessores')
    else:
        return render(request, 'formNovoProfessor.html', {'professor': professor})


def deletarProfessor(request, idprofessor):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
