from django import template

register = template.Library()


@register.filter(name='remove_tag')
def remove_tag(value, arg):
    return value.replace('+' + arg, '').replace(arg + '+', '').replace(arg, '')