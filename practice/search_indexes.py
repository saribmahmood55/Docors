from haystack import indexes
from practice.models import PracticeLocation


class PracticeLocationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.EdgeNgramField(model_attr='name')

    def get_model(self):
        return PracticeLocation

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
