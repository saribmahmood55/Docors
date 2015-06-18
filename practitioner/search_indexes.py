import datetime
from haystack import indexes
from practitioner.models import Practitioner


class PractitionerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    gender = indexes.CharField(model_attr='gender')

    def get_model(self):
        return Practitioner

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(status=True)