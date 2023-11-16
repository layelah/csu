from django.db import models


class Pharmacien(models.Model):
    STATUS = (
        ('Biologie', 'Biologie'),
        ('Pharmacologie', 'Pharmacologie'),
        ('Chimie', 'Chimie')
    )
    photo = models.ImageField(upload_to='pharmacien/images/', null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True)
    nom = models.CharField(max_length=100, null=True)
    specialite = models.CharField(max_length=200, null=True, choices=STATUS)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = "Pharmacien"
        verbose_name_plural = "Pharmaciens"
