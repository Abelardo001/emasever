from django.contrib import admin
from .models import Servico, Equipe, Cargo, BlogPost, Testemunho
# Register your models here.
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'icone', 'ativo', 'modificado')
@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ativo', 'modificado')

@admin.register(Testemunho)
class TestemunhoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')