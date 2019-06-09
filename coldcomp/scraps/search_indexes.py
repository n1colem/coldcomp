# search_indexes.py

from haystack import indexes
from scraps.models import Scrap, Mood

class ScrapIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    mood = indexes.CharField(model_attr='mood')

    def get_model (self) :
        return Scrap

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class MoodIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model (self) :
        return Mood
