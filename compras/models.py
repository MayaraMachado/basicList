from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length = 200)
    quantidade = models.IntegerField();

    def __str__(self):
        return self.nome;