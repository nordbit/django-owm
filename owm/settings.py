from django.conf import settings

APPID = getattr(settings, 'OWM_APPID', '')
CITIES = getattr(settings, 'OWM_CITIES', [])
