from django.views.generic import TemplateView
from settings import CITIES


class ForecastView(TemplateView):
    template_name = "owm/forecast.html"

    def get_context_data(self, **kwargs):
        context = super(ForecastView, self).get_context_data(**kwargs)
        context['cities'] = CITIES
        return context
