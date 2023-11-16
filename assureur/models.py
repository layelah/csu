from django.db import models


class Assureur(models.Model):
    STATUS = (
        ('mutuelle', 'mutuelle'), ('imputation budgétaire', 'imputation budgétaire'),
        ('IPM', 'IPM'), ('IPRES', 'IPRES'), ('FNR', 'FNR')
    )
    photo = models.ImageField(upload_to='assureur/images/', null=True, blank=True)
    libelle = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=25, null=True)
    adresse = models.CharField(max_length=100, null=True, blank=True)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, choices=STATUS)
    site_web = models.CharField(max_length=150, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Assureur"
        verbose_name_plural = "Assureurs"

    def __str__(self):
        return self.libelle
