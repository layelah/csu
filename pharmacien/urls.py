from django.urls import path
from . import views

urlpatterns = [
  path('liste_pharmacien/', views.vue_liste_pharmacien, name='liste_pharmacien'),
  path('<str:pk>', views.vue_details_pharmacien, name='details_pharmacien'),
  path('ajouter_pharmacien/', views.vue_ajouter_pharmacien, name='ajouter_pharmacien'),
  path('modification_pharmacien/<str:pk>/', views.vue_modification_pharmacien, name='modification_pharmacien'),
  path('supprimer_pharmacien/<str:pk>/', views.vue_supprimer_pharmacien, name='supprimer_pharmacien'),
]
