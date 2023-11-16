from django import forms
from .models import Pharmacie
from localisation.models import Departement, Commune


class PharmacieForm(forms.ModelForm):

    class Meta:
        model = Pharmacie
        fields = '__all__'
        labels = {
            'photo': 'photo',
            'libelle': 'libelle',
            'code': 'code',
            'adresse': 'adresse',
            'telephone': 'telephone',
            'email': 'Email',
            'type': 'type',
            'gerant': 'gerant',
        }
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'gerant': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departement'].queryset = Departement.objects.none()

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['departement'].queryset = (
                    Departement.objects.filter(region_id=region_id).order_by('libelle'))
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['departement'].queryset = self.instance.region.departement_set.order_by('libelle')

        self.fields['commune'].queryset = Commune.objects.none()

        if 'departement' in self.data:
            try:
                departement_id = int(self.data.get('departement'))
                self.fields['commune'].queryset = Commune.objects.filter(departement_id=departement_id).order_by(
                    'libelle')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['commune'].queryset = self.instance.departement.commune_set.order_by('libelle')
