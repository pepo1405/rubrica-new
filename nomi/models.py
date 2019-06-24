from django.db import models
from django.utils import timezone


class Rubrica(models.Model):
	# il campo author fa riferimento alla tabella User del progetto
	nome = models.CharField(max_length=200)
	indirizzo = models.TextField()
	telefono =  models.CharField(max_length=20, blank=True)
	cellulare =  models.CharField(max_length=20, blank=True)
	fax =  models.CharField(max_length=20, blank=True)
	email = models.EmailField(max_length=80,blank=True)
	def publish(self):
		self.save()

	def __str__(self):
		return self.nome
		
	class Meta:
		verbose_name="Rubrica"
		verbose_name_plural="Rubrica"
		
class Rubricar(models.Model):
	ragione_sociale = models.ForeignKey('Rubrica', on_delete=models.CASCADE)
	nome = models.CharField(max_length=200)
	incarico = models.CharField(max_length=200)
	telefono =  models.CharField(max_length=20, blank=True)
	cellulare =  models.CharField(max_length=20, blank=True)
	fax =  models.CharField(max_length=20, blank=True)
	email = models.EmailField(max_length=80,blank=True)

	def publish(self):
		self.save()

	def __str__(self):
		return self.ragione_sociale.nome+" "+self.nome
		
	class Meta:
		verbose_name="Nomi in Rubrica"
		verbose_name_plural="Nomi in Rubrica"
	
	