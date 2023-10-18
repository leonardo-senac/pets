from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vacina(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Anuncio(models.Model):
    CHOICES_GENERO = (
        ('M', 'Macho'),
        ('F', 'Fêmea')
    )

    titulo = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='imagens/')
    descricao = models.TextField(max_length=1536)
    genero = models.CharField(max_length=1, choices=CHOICES_GENERO)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    data_nascimento = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class vacinas_anuncios(models.Model):
    anuncio = models.ForeignKey(Anuncio, on_delete=models.PROTECT, related_name='vacinas')
    vacina = models.ForeignKey(Vacina, on_delete=models.PROTECT, blank=True)
    data_vacina = models.DateField()
    data_vencimento = models.DateField(null=True)