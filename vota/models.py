from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

# Create your models here.

class Consulta(models.Model):
	titol = models.CharField(max_length =200)
	text = models.TextField()
	propietari = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete =models.CASCADE)
	inici = models.DateTimeField()
	final = models.DateTimeField()
	def __str__(self):
		return self.titol

class Opcio(models.Model):
	consulta = models.ForeignKey(Consulta,on_delete =models.CASCADE)
	text = models.CharField(max_length =400)
	comentari = models.TextField(blank=True,null=True)
	def __str__(self):
		return self.text

class Invitacio(models.Model):
	consulta = models.ForeignKey(Consulta,on_delete =models.CASCADE)
	usuari = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete =models.CASCADE)
	enviada = models.BooleanField(default=False)
	acceptada = models.BooleanField(default=False)
	def __str__(self):
		return self.consulta.__str__() + " | " + self.usuari.__str__()

class Vot(models.Model):
	opcio = models.ForeignKey(Opcio,on_delete =models.CASCADE)
	consulta = models.ForeignKey(Consulta,on_delete =models.CASCADE)
	usuari = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete =models.CASCADE)
	def __str__(self):
		return self.usuari.__str__() \
			   + " | " + self.opcio.consulta.__str__() \
			   + " | " + self.opcio.__str__()

	'''class Meta:
		unique_together + ('usuari','consulta')
	'''
