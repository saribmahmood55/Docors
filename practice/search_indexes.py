import datetime
from haystack import indexes
from practice.models import Practice


class PracticeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    practice_type = indexes.CharField(model_attr='practice_type')
    modified = indexes.DateTimeField(model_attr='modified')

    def get_model(self):
        return Practice

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(practitioner__status=True)