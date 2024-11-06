from django.db import models

class Mobile(models.Model):
    nom = models.CharField(max_length=100)
    date_parution = models.DateField(blank=True, null = True)
    prix = models.FloatField(blank=False)
    constructeur = models.ForeignKey('Constructeur', on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return f"{self.nom} {self.date_parution} {self.prix} {self.constructeur}"
    
class Constructeur(models.Model):
    marque = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        return self.marque




