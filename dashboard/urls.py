from django.urls import path
from . import views

urlpatterns = [
  path('', views.vue_dashboard, name='dashboard'),
]
