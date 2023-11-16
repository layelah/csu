from django.contrib import admin
from .models import Pharmacien


@admin.register(Pharmacien)
class PharmacienAdmin(admin.ModelAdmin):
    list_display = ('code', 'prenom', 'nom', 'specialite', 'telephone', 'email')
    search_fields = ('code', 'prenom', 'nom', 'specialite', 'telephone', 'email')
    list_filter = ('specialite',)
