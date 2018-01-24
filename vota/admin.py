from django.contrib import admin

from .models import Consulta, Opcio, Invitacio, Vot

# Register your models here.

admin.site.register(Consulta)
admin.site.register(Opcio)
admin.site.register(Invitacio)
admin.site.register(Vot)