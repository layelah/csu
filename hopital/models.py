from django.db import models
from localisation.models import Region, Departement, Commune


class Prestation(models.Model):
    libelle = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Prestation"
        verbose_name_plural = "Prestations"

    def __str__(self):
        return self.libelle


class Hopital(models.Model):
    STATUS = (('clinique', 'clinique'), ('centre de santé public', 'centre de santé public'),
              ('poste de santé', 'poste de sante'), ('centre de santé privée', 'centre de santé privée'))

    photo = models.ImageField(upload_to='hopital/images/', null=True, blank=True)
    libelle = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=25, null=True)
    adresse = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, choices=STATUS)
    site_web = models.CharField(max_length=150, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Hopital"
        verbose_name_plural = "Hopitaux"

    def __str__(self):
        return self.libelle


class PriseEnCharge(models.Model):
    mon_hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)
    ma_prestation = models.ForeignKey(Prestation, on_delete=models.CASCADE)
    prix = models.FloatField(null=True)

    class Meta:
        verbose_name = "Prise en charge"
        verbose_name_plural = "Prises en charge"
