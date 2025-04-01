# mix/models.py

from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    detalhes = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')  # Imagens serão armazenadas na pasta 'media/produtos/'

    def __str__(self):
        return self.nome