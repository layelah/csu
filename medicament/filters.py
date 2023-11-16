import django_filters
from .models import Medicament


class MedicamentFilter(django_filters.FilterSet):
    nom_commercial = django_filters.CharFilter(lookup_expr='istartswith', label='Nom Commercial')
    dosage = django_filters.CharFilter(lookup_expr='istartswith', label='Dosage')
    forme_pharmaceutique = django_filters.CharFilter(lookup_expr='istartswith', label='Forme Pharmaceutique')
    prix = django_filters.RangeFilter(label='Prix')
    laboratoire = django_filters.CharFilter(lookup_expr='istartswith', label='Laboratoire')
    numero_autorisation = django_filters.CharFilter(lookup_expr='istartswith', label='Numéro Autorisation')
    date_autorisation = django_filters.DateFilter(label='Date d\'Autorisation')
    eligible = django_filters.BooleanFilter(label='Éligible')
    
    class Meta:
        model = Medicament
        fields = []
