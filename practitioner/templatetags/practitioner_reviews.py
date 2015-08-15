from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def get_rating_by_model(value, autoescape=True):
    final_str = ''
    review_val = value.get_count()
    for i in range(5):
        if i < int(review_val):
            final_str = final_str + '<li><i class="fa fa-star text-yellow"></i></li>'
        else:
            final_str = final_str + '<li><i class="fa fa-star text-gray"></i></li>'
    return mark_safe(final_str)
@register.filter(needs_autoescape=True)
def get_rating_by_count(value, autoescape=True):
    final_str = ''
    for i in range(5):
        if i < int(value):
            final_str = final_str + '<li><i class="fa fa-star text-yellow"></i></li>'
        else:
            final_str = final_str + '<li><i class="fa fa-star text-gray"></i></li>'
    return mark_safe(final_str)
