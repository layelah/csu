from django.urls import path
from . import views

urlpatterns = [
  path('liste_medecin/', views.vue_liste_medecin, name='liste_medecin'),
  path('<str:pk>', views.vue_details_medecin, name='details_medecin'),
  path('ajouter_medecin/', views.vue_ajouter_medecin, name='ajouter_medecin'),
  path('modification_medecin/<str:pk>/', views.vue_modification_medecin, name='modification_medecin'),
  path('supprimer_medecin/<str:pk>/', views.vue_supprimer_medecin, name='supprimer_medecin'),
]
