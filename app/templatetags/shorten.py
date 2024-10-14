from django import template

register = template.Library()

@register.filter
def shorten(value):
    if '-' in value:
        return value.split('-')[0]
    return value