from django.db import models


class Medicament(models.Model):
    photo = models.ImageField(upload_to='medicament/images/', null=True, blank=True)
    nom_commercial = models.CharField(max_length=100, null=True)
    dosage = models.CharField(max_length=50, null=True)
    forme_pharmaceutique = models.CharField(max_length=100, null=True)
    prix = models.FloatField(null=True)
    laboratoire = models.CharField(max_length=100, null=True)
    numero_autorisation = models.CharField(max_length=20, null=True)
    date_autorisation = models.DateField(null=True)
    presentation = models.TextField(null=True, blank=True)
    eligible = models.BooleanField(null=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom_commercial

    class Meta:
        verbose_name = "Medicament"
        verbose_name_plural = "Medicaments"
