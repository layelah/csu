from django.urls import path
from . import views

urlpatterns = [
  path('liste_hopital/', views.vue_liste_hopital, name='liste_hopital'),
  path('<str:pk>', views.vue_details_hopital, name='details_hopital'),
  path('ajouter_hopital/', views.vue_ajouter_hopital, name='ajouter_hopital'),
  path('modification_hopital/<str:pk>/', views.vue_modification_hopital, name='modification_hopital'),
  path('supprimer_hopital/<str:pk>/', views.vue_supprimer_hopital, name='supprimer_hopital'),

  path('ajax/chargement_departement/', views.chargement_departement, name='ajax_chargement_departement'),
  path('ajax/chargement_commune/', views.chargement_commune, name='ajax_chargement_commune'),
]
