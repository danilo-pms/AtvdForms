from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nome
    
    
class Aluno(models.Model):
    STATUS_CHOICES = [
        ('alimentos', 'Alimentos'),
        ('apicultura', 'Apicultura'),
        ('informatica', 'Informática')
    ]
    nome = models.CharField(max_length=150) 
    endereco = models.CharField(max_length=150)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=11, choices=STATUS_CHOICES)
    img = models.ImageField(upload_to='imagem/')
    
    def __str__(self):
        return self.nome
    
    