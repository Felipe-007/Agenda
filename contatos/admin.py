from django.contrib import admin
from .models import Categoria, Contato  #importará de models a categoria e contato

"""
Área administrativa
"""

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'categoria', 'mostrar')
    list_display_links = ('id', 'nome', 'sobrenome')  #faz virar links
    list_filter = ('nome', 'sobrenome')  #adicona o filtro
    list_per_page = 10  #será exibido 10 registros por pagina
    search_fields = ('nome', 'sobrenome')  #irá inserir um campo de pesquisa
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)  #ContatoAdmin apresenta a coluna nome e sobrenome
