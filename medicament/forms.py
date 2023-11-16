from django import forms
from .models import Medicament


class MedicamentForm(forms.ModelForm):

    class Meta:
        model = Medicament
        fields = '__all__'
        labels = {
            'photo': 'Photo',
            'nom_commercial': 'Nom Commercial',
            'dosage': 'Dosage',
            'forme_pharmaceutique': 'Forme Pharmaceutique',
            'prix': 'Prix',
            'laboratoire': 'Laboratoire',
            'numero_autorisation': 'Numéro d\'Autorisation',
            'date_autorisation': 'Date d\'Autorisation',
            'presentation': 'Présentation',
            'eligible': 'Éligible',
        }
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'nom_commercial': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'forme_pharmaceutique': forms.TextInput(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'laboratoire': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_autorisation': forms.TextInput(attrs={'class': 'form-control'}),
            'date_autorisation': forms.DateInput(attrs={'class': 'form-control'}),
            'presentation': forms.Textarea(attrs={'class': 'form-control'}),
            'eligible': forms.CheckboxInput(attrs={'class': 'form-control'}),
        }
