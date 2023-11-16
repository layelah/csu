from django.contrib import admin
from .models import Departement, Region, Commune


admin.site.register(Region)
admin.site.register(Departement)
admin.site.register(Commune)
