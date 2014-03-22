from django.conf.urls import patterns, url
from models import *
from views import ForecastView

urlpatterns = patterns('',
    url(r'^forecast/$', ForecastView.as_view(), name='owm-forecast'),
)
