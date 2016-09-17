from django.contrib.sitemaps import Sitemap
from practitioner.models import Practitioner


class PractitionerSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Practitioner.objects.all()

    def lastmod(self, obj):
        return obj.modified
