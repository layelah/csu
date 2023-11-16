from django.contrib import admin
from .models import *


@admin.register(Pharmacien)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'specialite', 'telephone', 'email', 'pharmacie',)
    search_fields = ('prenom', 'nom', 'specialite', 'telephone', 'email', 'pharmacie',)
    list_filter = ('specialite',)
