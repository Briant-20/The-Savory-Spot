from django.shortcuts import render, redirect
from .models import Year, Month, Day, Time, Table, Reservation
from django.views import View
import thesavoryspot.settings as django_settings
import smtplib
import ssl
from email.message import EmailMessage
import os


class ReservationView(View):
    template_name = 'reservation.html'

    def get(self, request):
        current_year = django_settings.CURRENT_YEAR
        reservation = request.session.get('reserved', False)
        request.session.pop('reserved', None)
        booked = request.session.get('booked', False)
        request.session.pop('booked', None)
        user_reservations = ""
        if request.user.is_authenticated:
            user_reservations = Reservation.objects.filter(user=request.user)
        context = {
            'current_year': current_year,
            'monthRange': range(12),
            'timeRange': [16, 17, 18, 19, 20],
            'reserved': reservation,
            'booked': booked,
            'user_reservations': user_reservations,
        }
        return render(request, self.template_name, context)

    def post(self, request):
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
                table=table_instance,
                user=request.user
            )

            subject = 'Reservation'
            body = f"""Hello {request.user}

Thank you for your recent booking.
Your table is reserved for {day_instance}/{month_instance}/{year_instance} at {time_instance}

Kind regards,
The Savory Spot
            """

            email_sender = os.environ.get("email_sender")
            email_password = os.environ.get("email_password")
            email_receiver = request.user.email

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

            request.session['reserved'] = True
            return redirect('reservation')
