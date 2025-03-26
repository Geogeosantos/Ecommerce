from django.db import models

class camisa(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    cor = models.CharField(max_length=100, null=False, blank=False)
    tamanho = models.CharField(max_length=100, null=False, blank=False)
    preco = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to="media/camisa1", blank=True)

    def __str__(self):
        return self.nome
    
class calca(models.Model):

    nome = models.CharField(max_length=100, null=False, blank=False)
    cor = models.CharField(max_length=100, null=False, blank=False)
    tamanho = models.CharField(max_length=100, null=False, blank=False)
    preco = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to="media/calca1", blank=True)

    def __str__(self):
        return self.nome