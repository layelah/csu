from django.contrib import admin
from .models import Pharmacie


@admin.register(Pharmacie)
class PharmacieAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'code', 'adresse', 'telephone', 'email', 'gerant', 'type')
    search_fields = ('libelle', 'code', 'adresse', 'telephone', 'email', 'gerant', 'type')
    list_filter = ('type',)
