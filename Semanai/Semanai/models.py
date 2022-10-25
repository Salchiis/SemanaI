from django.db import models

class miembros(models.Model):
    name = models.CharField("Nombre", max_length=50)
    description = models.TextField()
    profilePicture = models.ImageField(
        upload_to='static/img', null=True, blank=True)
    def _str_(self):
        return self.name