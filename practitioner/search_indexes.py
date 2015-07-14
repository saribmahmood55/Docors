# flake8: noqa
from haystack import indexes
from practitioner.models import Practitioner, Specialization, Condition, Procedure, Fellowship


class PractitionerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.EdgeNgramField(model_attr='full_name')

    def get_model(self):
        return Practitioner

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(status=True)


class FellowshipIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	name = indexes.EdgeNgramField(model_attr='name')
	
	def get_model(self):
		return Fellowship

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


class SpecializationIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	name = indexes.EdgeNgramField(model_attr='human_name')

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