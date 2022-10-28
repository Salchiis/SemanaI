from email.policy import default
from turtle import title
from django.db import models

class miembros(models.Model):
    name = models.CharField("Nombre", max_length=50)
    description = models.TextField()
    profilePicture = models.ImageField(
        upload_to='static/img', null=True, blank=True)
    def __str__(self):
        return self.name


class secciones(models.Model):
    title = models.CharField("Titulo", max_length=50)
    description = models.CharField("Descripcion", max_length=500)

    def __str__(self):
        return self.title


class tarjetas(models.Model):
    title = models.CharField("Titulo", max_length=50, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    picture = models.ImageField(upload_to='static/img', null=True, blank=True)
    seccion = models.ForeignKey(secciones, on_delete=models.CASCADE)
    principal = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class panel(models.Model):
    title = models.CharField("Titulo", max_length=50, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    picture = models.ImageField(upload_to='static/img', null=True, blank=True)
    
    def __str__(self):
        return self.title
