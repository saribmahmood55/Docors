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