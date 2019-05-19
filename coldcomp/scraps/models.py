from django.db import models
from django.utils import timezone

# Create your models here.
#scraps are like tiny blogs and concepts. they should be really shortand just text based.
#they are also like lists and stuff, and you can come back and edit them, so its important
#that they record updates
#they have moods

class Scrap(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField(blank=True)
    posted = models.DateTimeField(default=timezone.now)
    mood = models.ForeignKey('Mood', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "%s (%s)" % (self.title)

class Mood(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
