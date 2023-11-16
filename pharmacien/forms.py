from django import forms
from .models import Pharmacien


class PharmacienForm(forms.ModelForm):

    class Meta:
        model = Pharmacien
        fields = '__all__'
        labels = {
            'photo': 'photo',
            'code': 'code',
            'prenom': 'prenom',
            'nom': 'nom',
            'specialite': 'specialite',
            'telephone': 'telephone',
            'email': 'Email',
        }
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'specialite': forms.Select(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
