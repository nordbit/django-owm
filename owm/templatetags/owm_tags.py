from django import template
from owm.models import Weather, Forecast
from datetime import datetime

register = template.Library()


def get_weather(context, city, country):
    return {
        'weather': Weather.get_values(city, country),
        'city': city,
        'country': country,
    }
# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('owm/templatetags/weather.html', takes_context=True)(get_weather)


def get_forecast(context, city, country):
    return {
        'forecast': Forecast.get_values(city, country),
        'city': city,
        'country': country,
        'date_now': datetime.now().strftime("%d.%m.%Y."),
    }
# Register the custom tag as an inclusion tag with takes_context=True.
register.inclusion_tag('owm/templatetags/forecast.html', takes_context=True)(get_forecast)


@register.filter
def to_date(timestamp):
    try:
        #assume, that timestamp is given in seconds with decimal point
        ts = int(timestamp)
    except ValueError:
        return None

    return datetime.fromtimestamp(ts)


@register.filter
def to_int(value):
    try:
        return int(value)
    except:
        pass
