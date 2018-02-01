from django.contrib import admin

from .models import Consulta, Opcio, Invitacio, Vot

# Register your models here.
class ChoiceInLine(admin.StackedInline):
	model = Opcio
	extra = 2

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('titol', 'text', 'propietari', 'inici', 'final')
	readonly_fields = ['propietari']
	inlines = [ChoiceInLine]
	def save_model(self, request, obj, form, change):
		obj.propietari = request.user
		super(QuestionAdmin,self).save_model(request,obj,form,change)

	def get_queryset(self, request):
		query = super().get_queryset(request)
		if request.user.is_superuser:
			return query
		return query.filter(propietari=request.user)

class ChoiceAdmin(admin.ModelAdmin):
	list_display = ('consulta', 'text','vots_totals', 'propietari')
	readonly_fields = ('consulta','text')
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