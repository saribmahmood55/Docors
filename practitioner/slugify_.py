from practitioner.models import *
from django.template.defaultfilters import slugify
for obj in PractiseLocation.objects.all():
        obj.slug = slugify(obj.name)
        obj.save()