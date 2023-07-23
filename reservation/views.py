from django.shortcuts import render, redirect
from .models import Year, Month, Day, Time, Table, Reservation
from django.views import View
import thesavoryspot.settings as django_settings


class ReservationView(View):
    template_name = 'reservation.html'

    def get(self, request):
        current_year = django_settings.CURRENT_YEAR
        reservation = request.session.get('reserved', False)
        request.session.pop('reserved', None)
        booked = request.session.get('booked', False)
        request.session.pop('booked', None)

        context = {
            'current_year': current_year,
            'monthRange': range(12),
            'timeRange': [16, 17, 18, 19, 20],
            'reserved': reservation,
            'booked': booked,
        }
        return render(request, self.template_name, context)


def create_reservation(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        month = request.POST.get('month')
        day = request.POST.get('day')
        time = request.POST.get('time')

        year_instance, _ = Year.objects.get_or_create(year=year)
        month_instance, _ = Month.objects.get_or_create(years=year_instance, month=month)
        day_instance, _ = Day.objects.get_or_create(months=month_instance, day=day)
        time_instance, _ = Time.objects.get_or_create(days=day_instance, time=time)

        existing_reservations_count = Reservation.objects.filter(
            year=year_instance,
            month=month_instance,
            day=day_instance,
            time=time_instance,
        ).count()

        max_reservations = 3
        if existing_reservations_count < max_reservations:
            table_instance, _ = Table.objects.get_or_create(times=time_instance, table=str(existing_reservations_count+1))

        else:
            request.session['booked'] = True
            return redirect('reservation')

        Reservation.objects.create(
            year=year_instance,
            month=month_instance,
            day=day_instance,
            time=time_instance,
            table=table_instance
        )

        request.session['reserved'] = True
        return redirect('reservation')
