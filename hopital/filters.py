import django_filters
from .models import Hopital
from localisation.models import Region, Departement, Commune


class HopitalFilter(django_filters.FilterSet):
    libelle = django_filters.CharFilter(lookup_expr='istartswith', label='Libellé')
    code = django_filters.CharFilter(lookup_expr='istartswith', label='Code')
    type = django_filters.ChoiceFilter(choices=Hopital.STATUS, label='Type')
    adresse = django_filters.CharFilter(lookup_expr='istartswith', label='Adresse')
    telephone = django_filters.CharFilter(lookup_expr='istartswith', label='Téléphone')
    email = django_filters.CharFilter(lookup_expr='istartswith', label='Email')
    site_web = django_filters.CharFilter(lookup_expr='istartswith', label='Site_web')
    region = django_filters.ModelChoiceFilter(queryset=Region.objects.all(), label='Région')
    departement = django_filters.ModelChoiceFilter(queryset=Departement.objects.all(), label='Département')
    commune = django_filters.ModelChoiceFilter(queryset=Commune.objects.all(), label='Commune')

    class Meta:
        model = Hopital
        fields = []
