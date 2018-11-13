"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Artist(models.Model):
    '''model for the Artist in database'''
    name = models.CharField("artist", max_length = 50)
    year_formed = models.PositiveIntegerField()


class Album(models.Model):
    '''model for Album in database'''
    name = models.CharField("album", max_length = 50)
    artist = models.ForeignKey(Artist)