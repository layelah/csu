from django.db import models


class Region(models.Model):
    libelle = models.CharField(max_length=40)

    def __str__(self):
        return self.libelle


class Departement(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=40)

    def __str__(self):
        return self.libelle


class Commune(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    libelle = models.CharField(max_length=40)

    def __str__(self):
        return self.libelle
