from practice.models import City, RecentSearch
from practitioner.models import Specialization

def updateRecentSearches(city, spec):
	if city != '' and spec != '':
		citi = City.objects.get(slug=city)
		speciality = Specialization.objects.get(slug=spec)
		try:
			obj = RecentSearch.objects.get(city=citi, speciality=speciality)
			obj.hit_count+=1
			obj.save()
		except:
			obj = RecentSearch.objects.create(city=citi, speciality=speciality, hit_count=1)

def get_review_details(reviews):
	answers_avg = {'anw1':0,'anw2':0,'anw3':0,'anw4':0,'anw5':0, 'num_of_reviews':len(reviews)}
	total = 0
	for review in reviews:
		answers_avg['anw1'] = answers_avg['anw1'] + review.answers.answer1
		answers_avg['anw2'] = answers_avg['anw2'] + review.answers.answer2
		answers_avg['anw3'] = answers_avg['anw3'] + review.answers.answer3
		answers_avg['anw4'] = answers_avg['anw4'] + review.answers.answer4
		answers_avg['anw5'] = answers_avg['anw5'] + review.answers.answer5
		review['per_review'] = (review.answers.answer1+review.answers.answer2+review.answers.answer3+review.answers.answer4+review.answers.answer5)/5
	for i in range(1,6):
		if len(reviews):
			answers_avg['anw'+str(i)] = answers_avg['anw'+str(i)] / len(reviews)
			total = total + answers_avg['anw'+str(i)]
	answers_avg['total'] = total/5
	print answers_avg
	return answers_avg