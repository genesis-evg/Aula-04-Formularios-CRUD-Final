from django.db import models

# Create your models here.
from django.db.models.fields import BooleanField


class ranking(models.Model):
  nome = models.CharField(max_length=100)
  icone = models.CharField(max_length=100)
  descricao = models.TextField(blank=True)
  modalidade = models.CharField(max_length=20)
  relevancia = models.IntegerField()

  def __str__(self):
   return self.nome


class link(models.Model):
  nome = models.CharField(max_length=100)
  link = models.URLField(max_length=1000)
  ref_ranking = models.ForeignKey(ranking,
                          on_delete=models.CASCADE)
  descricao = models.TextField(max_length=1000)
  cadastrado = BooleanField(default=False)
  def __str__(self):
    return self.nome

