# models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Pedido(models.Model):
    SEGMENTO_CHOICES = [
        ('batizado', 'Batizado'),
        ('debutante', 'Debutante'),
        ('casamento', 'Casamento'),
        ('aniversario', 'Aniversário'),
    ]

    MASSA_CHOICES = [
        ('baunilha', 'Baunilha'),
        ('cenoura', 'Cenoura'),
        ('paodelo', 'Pão de Ló'),
        ('festa', 'Festa'),
    ]

    RECHEIO_CHOICES = [
        ('brigadeiro', 'Brigadeiro'),
        ('docedeleite', 'Doce de Leite'),
        ('abacaxi', 'Abacaxi'),
        ('morango', 'Morango'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos_user')
    segmento = models.CharField(max_length=20, choices=SEGMENTO_CHOICES)
    massa = models.CharField(max_length=20, choices=MASSA_CHOICES)
    recheio = models.CharField(max_length=20, choices=RECHEIO_CHOICES)
    data_de_entrega = models.DateField()
    detalhes = models.TextField()
    contato = models.CharField(max_length=20)

    def __str__(self):
        return f" Pedido {self.segmento} - Pedido {self.user.username}"