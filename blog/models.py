from django.db import models
from datetime import datetime

# Create your models here.
class Postagem(models.Model):
	class Meta:
		ordering = ('-publicacao',)
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField()
	publicacao = models.DateTimeField(default=datetime.now, blank=True)
	categoriaprincipal = models.CharField(max_length=50)
	categoriassecundarias= models.CharField(max_length=100)
	autor = models.CharField(max_length=100)

	def get_absolute_url(self):
		return '/post/%s'%self.titulo
