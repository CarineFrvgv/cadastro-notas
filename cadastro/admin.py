from django.contrib import admin

# Register your models here.
from .models import Aluno, Materia, Nota

admin.site.register(Aluno)
admin.site.register(Materia)
admin.site.register(Nota)