from django.contrib import admin
from django.contrib.auth.models import User
from reviews.models import Review, ReviewStats

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
	list_display = ['practitioner','patient','practise','review_text','review_date','up_votes','down_votes','post_as_anonymous']
	list_filter = ['review_date']

	def Practitioner_Reviewed(self, obj):
		return obj.practitioner.name

	def Reviewed_By(self, obj):
		return "%s %s" % (obj.patient.user.first_name, obj.patient.user.last_name)


class ReviewStatsAdmin(admin.ModelAdmin):
	list_display = ['patient','review','status']


admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewStats, ReviewStatsAdmin)