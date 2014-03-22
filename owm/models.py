from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
import json
import jsonfield
import urllib2

from django.utils.timezone import now
from settings import APPID


def get_weather(city, country):
    url = "http://api.openweathermap.org/data/2.5/weather?q=%(city)s,%(country)s&units=metric&APPID=%(appid)s" % {
        'city': city,
        'country': country,
        'appid': APPID,
    }
    data = {}
    try:
        req = urllib2.Request(url, None)
        opener = urllib2.build_opener()
        f = opener.open(req)
        data = json.load(f)
    except:
        pass
    return data


def get_forecast(city, country):
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%(city)s,%(country)s&units=metric&APPID=%(appid)s&cnt=7" % {
        'city': city,
        'country': country,
        'appid': APPID,
    }
    data = {}
    try:
        req = urllib2.Request(url, None)
        opener = urllib2.build_opener()
        f = opener.open(req)
        data = json.load(f)
    except:
        pass
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
            if hours > 3:
                obj.values = get_weather(city, country)
                obj.last_modified = now()
                obj.save()
        except ObjectDoesNotExist:
            obj = cls(city=city, country=country)
            obj.values = get_weather(city, country)
            obj.save()
        return obj.values


class Forecast(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    last_modified = models.DateTimeField(_("Last modified"), null=True, blank=True, db_index=True, default=now)
    values = jsonfield.JSONField()

    @classmethod
    def get_values(cls, city, country):
        try:
            obj = cls.objects.get(city=city, country=country)
            hours = (now() - obj.last_modified).seconds / 3600
            if hours > 8:
                obj.values = get_forecast(city, country)
                obj.last_modified = now()
                obj.save()
        except ObjectDoesNotExist:
            obj = cls(city=city, country=country)
            obj.values = get_forecast(city, country)
            obj.save()
        return obj.values
