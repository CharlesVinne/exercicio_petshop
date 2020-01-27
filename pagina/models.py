from django.db import models


# Create your models here.

class Pet(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    tipos = (
        ('GATO', 'Gato'),
        ('CACHORRO', 'Cachorro'),
        ('AVES', 'Aves')
    )
    tipo = models.CharField(choices=tipos, max_length=100)
    dono = models.CharField(max_length=100)

class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_de_nascimento = models.CharField(max_length=10)
    email = models.EmailField()
    cep = models.CharField(max_length=9)
    numero = models.IntegerField()
    genero = (
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),
        ('OUTROS', 'Outros')
    )
    celular = models.CharField(max_length=14)
    motivo = models.TextField()

class Ong(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=14)
    tempo_duracao = models.CharField(max_length=100)
