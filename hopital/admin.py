from django.contrib import admin
from .models import Hopital, Prestation, PriseEnCharge


@admin.register(Prestation)
class PrestationAdmin(admin.ModelAdmin):
    list_display = ('libelle',)
    search_fields = ('libelle',)
    list_filter = ('libelle',)


@admin.register(Hopital)
class HopitalAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'code', 'adresse', 'telephone', 'email', 'type')
    search_fields = ('libelle', 'code', 'adresse', 'telephone', 'email', 'type')
    list_filter = ('type',)


@admin.register(PriseEnCharge)
class PriseEnChargeAdmin(admin.ModelAdmin):
    list_display = ('mon_hopital', 'ma_prestation', 'prix',)
    search_fields = ('mon_hopital', 'ma_prestation', 'prix',)
