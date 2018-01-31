from django.contrib import admin

from .models import Consulta, Opcio, Invitacio, Vot

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['titol', 'text', 'propietari', 'inici', 'final']
    list_display = ('titol', 'text', 'propietari', 'inici', 'final')
    def get_queryset(self, request):
    	query = super().get_queryset(request)
    	if request.user.is_superuser:
    		return query
    	return query.filter(propietari=request.user)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('consulta', 'text', 'vots')

    def get_queryset(self, request):
    	us = Opcio.objects.all()
    	super().get_queryset(request)
    	if request.user.is_superuser:
    		return us
    	return us.filter(consulta__propietari=request.user)

admin.site.register(Consulta, QuestionAdmin)
admin.site.register(Opcio, ChoiceAdmin)
admin.site.register(Invitacio)
admin.site.register(Vot)