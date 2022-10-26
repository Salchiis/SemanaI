from turtle import title
from django.db import models

class miembros(models.Model):
    name = models.CharField("Nombre", max_length=50)
    description = models.TextField()
    profilePicture = models.ImageField(
        upload_to='static/img', null=True, blank=True)
    def __str__(self):
        return self.name
    
class seccion(models.Model):
    title = models.CharField("Título",max_length = 50)
    description = models.TextField()
    def __str__(self):
        return self.title

class card(models.Model):
    title = models.CharField("Título",max_length = 50)
    description = models.TextField()
    profilePicture = models.ImageField(
        upload_to='static/img', null=True, blank=True)
    def __str__(self):
        return self.title