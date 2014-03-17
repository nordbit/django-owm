from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
import json
import jsonfield
import urllib2

from django.utils.timezone import now

APPID="533d7e39b3384f90460faa73b55f8f8f"

def get_weather(city, country):
    url = "http://api.openweathermap.org/data/2.5/weather?q=%(city)s,%(country)s&units=metric&APPID=%(appid)s" % {
        'city': city,
        'country': country,
        'appid': APPID,
    }
    req = urllib2.Request(url, None)
    opener = urllib2.build_opener()
    f = opener.open(req)
    data = json.load(f)
    return data

class Weather(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    last_modified = models.DateTimeField(_("Last modified"), null=True, blank=True, db_index=True, default=now)
    values = jsonfield.JSONField()

    @classmethod
    def get_values(cls, city, country):
        try:
            obj = cls.objects.get(city=city, country=country)
            hours = (now() - obj.last_modified).seconds / 3600
            if hours > 1:
                obj.values = get_weather(city, country)
                obj.last_modified = now()
                obj.save()
        except ObjectDoesNotExist:
            obj = cls(city=city, country=country)
            obj.values = get_weather(city, country)
            obj.save()
        return obj.values
