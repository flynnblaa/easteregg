from django.db import models

from geopy.distance import vincenty
from random import choice
from string import digits, ascii_uppercase
from os.path import splitext

# Create your models here.

class Egg(models.Model):
    sequenceNumber = models.IntegerField()
    locationName = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    radius = models.FloatField()
    textClue = models.TextField(blank=True)
    visits = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    levelJustEnded = models.IntegerField(default=None, blank=True, null=True)
    finalEnd = models.BooleanField(default=False)

    def __str__(self):
        return str(self.sequenceNumber)+". "+str(self.locationName)

    def isClose(self, observerLatitude, observerLongitude):
        # Use the awesome module from Python - no more actual formulae!
        egg = (self.latitude, self.longitude)
        hunter = (observerLatitude, observerLongitude)
        return vincenty(egg, hunter).meters <= self.radius

    def visit(self):
        self.visits+=1
        self.save()


def random_filename(instance, filename):
    _, extension = splitext(filename)
    return 'clueimage/' + ''.join(choice(ascii_uppercase + digits) for _ in range(12)) + extension

class Image(models.Model):
    egg = models.ForeignKey(Egg)
    image = models.ImageField(upload_to=random_filename)



class LeaderboardEntry(models.Model):
    name = models.CharField(max_length=255)
    ipAddress = models.CharField(max_length=100)
    publicationDate = models.DateTimeField('Entry time')
    level = models.IntegerField(default=1)

    def __str__(self):
        return self.name

