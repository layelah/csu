from django.db import models
from hopital.models import Hopital


class Medecin(models.Model):
    STATUS = (
        ('Virologie', 'Virologie'),
        ('Cancerologie', 'Cancerologie'),
        ('Pediatrie', 'Pediatrie')
    )
    photo = models.ImageField(upload_to='medecin/images/', null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True)
    nom = models.CharField(max_length=100, null=True)
    specialite = models.CharField(max_length=150, null=True, choices=STATUS)
    telephone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    hopitaux = models.ManyToManyField(Hopital, related_name='medecins')
    date_ajout = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        verbose_name = "Medecin"
        verbose_name_plural = "Medecins"
