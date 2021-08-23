from django.db import models
from django.utils import timezone

"""
Models.py
é onde são criadas as tabelas para o banco de dados sqlite3
apos criada, será preciso migrar para o banco
python manage.py makemigrations
python manage.py migrate
"""

"""
CONTATOS
nome: STR * (obrigatório)
sobrenome: STR (opcional)
telefone: STR * (obrigatório)
email: STR (opcional)
data_criação: DATETIME (automático)
descrição: texto
categoria: CATEGORIA (outro model)

CATEGORIA
nome: STR * (obrigatório)
"""

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome  #irá apresentar o nome, ao inves da str inteira


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)  #faz a referencia entre a tabela Contato e Categoria, não irá fazer nada caso o campo categoria seja apagado
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')  #upload de imagens

    def __str__(self):
        return self.nome