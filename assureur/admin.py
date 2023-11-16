from django.contrib import admin
from .models import Assureur


@admin.register(Assureur)
class AssureurAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'code', 'adresse', 'telephone', 'email', 'type')
    search_fields = ('libelle', 'code', 'adresse', 'telephone', 'email', 'type')
    list_filter = ('type',)
