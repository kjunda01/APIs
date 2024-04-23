from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)


'''
from django.db import models

class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
'''