from django.shortcuts import render
from django.views import View
import thesavoryspot.settings as django_settings


class ReservationView(View):
    template_name = 'reservation.html'

    def get(self, request):
        current_year = django_settings.CURRENT_YEAR

        context = {
            'current_year': current_year,
            'monthRange': range(12),
            'dayRange': range(30),
        }

        return render(request, self.template_name, context)