"""
Definition of models.
"""

from django.db import models
#from django.forms import ModelForm
from django import forms

# Create your models here.

class Artist(models.Model):
    '''model for the Artist in database'''
    name = models.CharField("artist", max_length = 50)
    year_formed = models.PositiveIntegerField()

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'year_formed']


class Album(models.Model):
    '''model for Album in database'''
    name = models.CharField("album", max_length = 50)
    artist = models.ForeignKey(Artist)

#class AlbumForm(models.Model):
#    class Meta:
#        model = Album
#        fields = ['name', 'artist']