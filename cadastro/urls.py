from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('cadastrar', views.cadastrar_aluno, name="cadastrar_aluno"),
  path('alunos', views.alunos_cadastrados, name="alunos_cadastrados"),
  path('aluno/<int:id>', views.pagina_aluno, name="pagina_aluno"),
  path('aluno/<int:id>/nota', views.add_nota, name="add_nota")
]