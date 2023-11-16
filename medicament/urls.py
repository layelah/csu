from django.urls import path
from . import views

urlpatterns = [
  path('liste_medicament/', views.vue_liste_medicament, name='liste_medicament'),
  path('<str:pk>', views.vue_details_medicament, name='details_medicament'),
  path('ajouter_medicament/', views.vue_ajouter_medicament, name='ajouter_medicament'),
  path('modification_medicament/<str:pk>/', views.vue_modification_medicament, name='modification_medicament'),
  path('supprimer_medicament/<str:pk>/', views.vue_supprimer_medicament, name='supprimer_medicament'),
]
