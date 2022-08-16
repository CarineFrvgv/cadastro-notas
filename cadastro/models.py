from django.db import models

class Aluno(models.Model):
  nome = models.CharField(max_length=60)
  data_nascimento = models.DateField()
  numero_telefone = models.CharField("telefone", max_length=13)

class Materia(models.Model):
  nome = models.CharField("nome", max_length=30)
  alunos = models.ManyToManyField(Aluno, through='Nota')

class Nota(models.Model):
  aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
  materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
  unidade_1 = models.FloatField()
  unidade_2 = models.FloatField()
  unidade_3 = models.FloatField()
  unidade_4 = models.FloatField()

  def get_soma(self):
    return self.unidade_1 + self.unidade_2 + self.unidade_3 + self.unidade_4

  def get_media(self):
    return self.get_soma()/4