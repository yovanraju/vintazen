# your_app/templatetags/rupiah_filters.py

from django import template

register = template.Library()

@register.filter
def rupiah_format(value):
    try:
        value = int(value)
        return "Rp {:,}".format(value).replace(",", ".")
    except (ValueError, TypeError):
        return value
