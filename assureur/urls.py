from django.urls import path
from . import views

urlpatterns = [
  path('liste_assureur/', views.vue_liste_assureur, name='liste_assureur'),
  path('<str:pk>', views.vue_details_assureur, name='details_assureur'),
  path('ajouter_assureur/', views.vue_ajouter_assureur, name='ajouter_assureur'),
  path('modification_assureur/<str:pk>/', views.vue_modification_assureur, name='modification_assureur'),
  path('supprimer_assureur/<str:pk>/', views.vue_supprimer_assureur, name='supprimer_assureur'),
]
