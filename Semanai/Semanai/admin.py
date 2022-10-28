from atexit import register
from django.contrib import admin
from .models import *

admin.site.register(miembros)
admin.site.register(secciones)
admin.site.register(tarjetas)
admin.site.register(panel)

