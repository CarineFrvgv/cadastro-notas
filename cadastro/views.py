from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno, Materia, Nota


def index(request):
  return render(request, "cadastro/index.html")

# mostra lista de alunos cadastrados
def alunos_cadastrados(request):
  alunos = Aluno.objects.all().order_by('nome')

  return render(request, "cadastro/alunos_cadastrados.html", {"alunos":alunos})

# cadastro de novo aluno
def cadastrar_aluno(request):
  if request.method == "POST":
    dados = request.POST

    novo_aluno = Aluno(nome=dados.get('nome'), 
                       data_nascimento=dados.get("nascimento"), 
                       numero_telefone=dados.get("telefone"))
    novo_aluno.save()

    return redirect("pagina_aluno", id=novo_aluno.id)
    
  return render(request, "cadastro/cadastrar_aluno.html")

# pagina com informacoes de um aluno
def pagina_aluno(request, id):
  aluno_notas = Nota.objects.all().filter(aluno=id)
  aluno_info = Aluno.objects.get(id=id)

  return render(request, "cadastro/pagina_aluno.html", {"aluno": aluno_info, "notas": aluno_notas })


def add_nota(request, id):
  if request.method == "POST":
    # checar se a materia ja existe no banco de dados
    try: 
      materia = Materia.objects.get(nome=request.POST['materia'].lower())

    except Materia.DoesNotExist:
      materia = None

    if not materia:
      # criar a nova materia se ela nao existe
      materia = Materia(nome=request.POST['materia'].lower())
      materia.save()

    nova_nota = Nota(
                    aluno=Aluno.objects.get(id=id),
                    materia=materia, 
                    unidade_1=request.POST['u1'],
                    unidade_2=request.POST['u2'],
                    unidade_3=request.POST['u3'],
                    unidade_4=request.POST['u4'])
    nova_nota.save()

    return redirect('pagina_aluno', id=id)

  return render(request, 'cadastro/add_notas.html', {"id":id})