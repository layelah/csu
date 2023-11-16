from django.db import models
from pharmacien.models import Pharmacien
from localisation.models import Region, Departement, Commune


class Pharmacie(models.Model):
    STATUS = (
        ('clinique', 'clinique'),
        ('militaire', 'militaire'),
        ('veterinaire', 'veterinaire')
    )
    photo = models.ImageField(upload_to='pharmacie/images/', null=True, blank=True)
    libelle = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=25, null=True)
    adresse = models.CharField(max_length=100, null=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    gerant = models.ForeignKey(Pharmacien, on_delete=models.SET_NULL, null=True, related_name='pharmacie')
    type = models.CharField(max_length=100, null=True, choices=STATUS)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Pharmacie"
        verbose_name_plural = "Pharmacies"

        def __str__(self):
            return self.libelle
