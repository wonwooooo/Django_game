from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    titre = models.CharField(max_length=50)
    couverture = models.CharField(max_length=250)
    categorie = models.CharField(max_length=50)
    gameplay = models.CharField(max_length=250)
    prix = models.IntegerField()


    def __str__(self):
        return self.titre + ': ' + self.categorie


class Phone(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)


    def __str__(self):
        return f"{self.username : self.phone}"
