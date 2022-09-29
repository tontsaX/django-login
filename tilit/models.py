from enum import unique
from unicodedata import name
from django.contrib.auth.models import AbstractUser
from django.db import models

class Käyttäjä(AbstractUser):
    organization = models.ForeignKey('Organisaatio', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.organization}'

class Organisaatio(models.Model):
    name = models.CharField(max_length=200, help_text='Lisää organisaatiosi nimi.')

    def __str__(self):
        return self.name