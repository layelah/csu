from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compte/', include('compte.urls')),
    path('', include('accueil.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('pharmacien/', include('pharmacien.urls')),
    path('medecin/', include('medecin.urls')),
    path('pharmacie/', include('pharmacie.urls')),
    path('hopital/', include('hopital.urls')),
    path('medicament/', include('medicament.urls')),
    path('assureur/', include('assureur.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "accueil.views.handel404"
