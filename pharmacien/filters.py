import django_filters
from .models import Pharmacien


class PharmacienFilter(django_filters.FilterSet):
    prenom = django_filters.CharFilter(lookup_expr='istartswith', label='Prénom')
    nom = django_filters.CharFilter(lookup_expr='istartswith', label='Nom')
    code = django_filters.CharFilter(lookup_expr='istartswith', label='Code')
    specialite = django_filters.ChoiceFilter(choices=Pharmacien.STATUS, label='Spécialité')
    telephone = django_filters.CharFilter(lookup_expr='istartswith', label='Téléphone')
    email = django_filters.CharFilter(lookup_expr='istartswith', label='Email')

    class Meta:
        model = Pharmacien
        fields = []
