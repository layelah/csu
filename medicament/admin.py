from django.contrib import admin
from .models import Medicament


@admin.register(Medicament)
class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('nom_commercial', 'dosage', 'forme_pharmaceutique', 'prix', 'laboratoire', 'numero_autorisation',
                    'date_autorisation', 'eligible', 'presentation')
    search_fields = ('nom_commercial', 'dosage', 'forme_pharmaceutique', 'prix', 'laboratoire', 'numero_autorisation',
                     'date_autorisation', 'eligible', 'presentation')
    list_filter = ('eligible',)
