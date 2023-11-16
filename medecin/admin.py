from django.contrib import admin
from .models import Medecin


@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('code', 'prenom', 'nom', 'specialite', 'telephone', 'email')
    search_fields = ('code', 'prenom', 'nom', 'specialite', 'telephone', 'email')
    list_filter = ('specialite',)
