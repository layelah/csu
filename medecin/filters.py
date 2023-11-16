import django_filters
from .models import Medecin


class MedecinFilter(django_filters.FilterSet):
    prenom = django_filters.CharFilter(lookup_expr='istartswith', label='Prénom')
    nom = django_filters.CharFilter(lookup_expr='istartswith', label='Nom')
    code = django_filters.CharFilter(lookup_expr='istartswith', label='Code')
    specialite = django_filters.ChoiceFilter(choices=Medecin.STATUS, label='Spécialité')
    telephone = django_filters.CharFilter(lookup_expr='istartswith', label='Téléphone')
    email = django_filters.CharFilter(lookup_expr='istartswith', label='Email')

    class Meta:
        model = Medecin
        fields = []
