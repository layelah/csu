import django_filters
from .models import Assureur


class AssureurFilter(django_filters.FilterSet):
    libelle = django_filters.CharFilter(lookup_expr='istartswith', label='Libellé')
    code = django_filters.CharFilter(lookup_expr='istartswith', label='Code')
    type = django_filters.ChoiceFilter(choices=Assureur.STATUS, label='Type')
    adresse = django_filters.CharFilter(lookup_expr='istartswith', label='Adresse')
    telephone = django_filters.CharFilter(lookup_expr='istartswith', label='Téléphone')
    email = django_filters.CharFilter(lookup_expr='istartswith', label='Email')
    site_web = django_filters.CharFilter(lookup_expr='istartswith', label='Site_web')

    class Meta:
        model = Assureur
        fields = []
