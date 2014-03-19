from django import template
from owm.models import Weather

register = template.Library()

def get_weather(context, city, country):
    return {
        'weather': Weather.get_values(city, country),
        'city': city,
        'country': country,
    }
# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('owm/weather.html', takes_context=True)(get_weather)

@register.filter
def to_int(value):
    return int(value)
