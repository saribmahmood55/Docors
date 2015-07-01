from django.contrib import admin
from django.contrib.auth.models import User
from reviews.models import Review, Answer, Comment, Question

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
	list_display = ['practitioner','patient','answers','comments','anonymous','timestamp']
	list_filter = ['timestamp']

	def Practitioner_Reviewed(self, obj):
		return obj.practitioner.name

	def Reviewed_By(self, obj):
		return "%s %s" % (obj.patient.user.first_name, obj.patient.user.last_name)

class AnswerAdmin(admin.ModelAdmin):
	list_display = ['answer1','answer2','answer3','answer4','answer5']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['text','agree','disagree']

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['question1','question2','question3','question4','question5']


admin.site.register(Review, ReviewAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Question, QuestionAdmin)