import datetime
from haystack import indexes
from practitioner.models import Practitioner, Specialization, Condition, Procedure


class PractitionerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.EdgeNgramField(model_attr='name')
    gender = indexes.EdgeNgramField(model_attr='gender')

    def get_model(self):
        return Practitioner

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(status=True)

class SpecializationIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	name = indexes.EdgeNgramField(model_attr='SEO_name')


	def get_model(self):
		return Specialization

	def index_queryset(self, using=None):
		return self.get_model().objects.all()

class ProcedureIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	name = indexes.EdgeNgramField(model_attr='name')

	def get_model(self):
		return Procedure

	def index_queryset(self, using=None):
		return self.get_model().objects.all()

class ConditionIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	name = indexes.EdgeNgramField(model_attr='name')

	def get_model(self):
		return Condition

	def index_queryset(self, using=None):
		return self.get_model().objects.all()