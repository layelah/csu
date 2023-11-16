from django.urls import path
from . import views

urlpatterns = [
  path('liste_pharmacie/', views.vue_liste_pharmacie, name='liste_pharmacie'),
  path('<str:pk>', views.vue_details_pharmacie, name='details_pharmacie'),
  path('ajouter_pharmacie/', views.vue_ajouter_pharmacie, name='ajouter_pharmacie'),
  path('modification_pharmacie/<str:pk>/', views.vue_modification_pharmacie, name='modification_pharmacie'),
  path('supprimer_pharmacie/<str:pk>/', views.vue_supprimer_pharmacie, name='supprimer_pharmacie'),

  path('ajax/chargement_departement/', views.chargement_departement, name='ajax_chargement_departement'),
  path('ajax/chargement_commune/', views.chargement_commune, name='ajax_chargement_commune'),
]
