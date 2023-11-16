from django import forms
from .models import Assureur


class AssureurForm(forms.ModelForm):

    class Meta:
        model = Assureur
        fields = '__all__'
        labels = {
            'photo': 'photo',
            'libelle': 'libelle',
            'code': 'code',
            'adresse': 'adresse',
            'telephone': 'telephone',
            'email': 'Email',
            'type': 'type',
            'site_web': 'site_web',
        }
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'libelle': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'site_web': forms.TextInput(attrs={'class': 'form-control'}),
        }
