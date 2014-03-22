from django.conf.urls import patterns, url
from models import *

urlpatterns = patterns('',
	url(r'^forecast/$', ForecastView.as_view(), name='owm-forecast'),
)

