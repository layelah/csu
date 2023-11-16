from django.urls import path
from . import views

urlpatterns = [
    path('connexion/', views.vue_page_connexion, name="connexion"),
]
