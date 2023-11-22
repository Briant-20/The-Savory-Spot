from django.shortcuts import render, redirect
from .models import Year, Month, Day, Time, Table, Reservation
from django.views import View
from datetime import datetime
import smtplib
import ssl
from email.message import EmailMessage
import os


# Function to get context for rendering templates
def get_context(request):
    # Get current date and time information
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day
    current_hour = datetime.now().hour
    current_minute = datetime.now().minute
    current_time = current_hour + current_minute

    # Check session variables for reservation status
    reservation = request.session.get('reserved', False)
    request.session.pop('reserved', None)
    booked = request.session.get('booked', False)
    request.session.pop('booked', None)
    deleted = request.session.get('deleted', False)
    request.session.pop('deleted', None)

    # Get user reservations if user is authenticated
    user_reservations = ""
    if request.user.is_authenticated:
        user_reservations = Reservation.objects.filter(user=request.user)

    # Create context dictionary
    context = {
        'current_year': current_year,
        'current_month_range': range(current_month+1, 13),
        'current_month': current_month,
        'month_range': range(12),
        'current_day': current_day,
        'time_range': range(16, 21),
        'current_hour': current_hour,
        'current_hour_range': range(current_hour, 21),
        'current_minute': current_minute,
        'current_time': current_time,
        'reserved': reservation,
        'booked': booked,
        'deleted': deleted,
        'user_reservations': user_reservations,
    }
    return context


# Function to check existing reservations for a given date, time, and table
def check_existing_reservations(year_instance, month_instance, day_instance,
                                time_instance, table_instance):
    # Query the database for existing reservations
    existing_reservation = Reservation.objects.filter(
        year=year_instance,
        month=month_instance,
        day=day_instance,
        time=time_instance,
        table=table_instance,
    )
    return existing_reservation


def create(request):
    # Fetch email credentials from environment variables
    email_sender = os.environ.get("email_sender")
    email_password = os.environ.get("email_password")

    # Get the email of the requesting user
    email_receiver = request.user.email

    # Extract reservation details from the request
    year = request.POST.get('year')
    month = request.POST.get('month')

    # If month is not provided in the request, use the current month
    if month == "":
        month = request.POST.get('current_month')

    day = request.POST.get('day')
    time = request.POST.get('time')

    # If time is not provided in the request, use the current time
    if time == "":
        time = request.POST.get('current_time')

    # Get or create instances for Year, Month, Day, and Time
    year_instance, _ = Year.objects.get_or_create(year=year)
    month_instance, _ = Month.objects.get_or_create(
        years=year_instance, month=month)
    day_instance, _ = Day.objects.get_or_create(months=month_instance, day=day)
    time_instance, _ = Time.objects.get_or_create(days=day_instance, time=time)

    # Check the number of existing reservations for the given time slot
    existing_reservations_count = Reservation.objects.filter(
        year=year_instance,
        month=month_instance,
        day=day_instance,
        time=time_instance,
    ).count()

    # Set the maximum number of reservations allowed
    max_reservations = 3

    # If there is still space for reservations, create a new table instance
    if existing_reservations_count < max_reservations:
        table_instance, _ = Table.objects.get_or_create(
            times=time_instance, table=str(existing_reservations_count + 1))
    else:
        # If all slots are booked, set a flag in the session and return
        request.session['booked'] = True
        return False

    # Iterate over the possible table numbers and find the first available one
    for i in range(max_reservations):
        existing_reservation = check_existing_reservations(
            year_instance, month_instance,
            day_instance, time_instance, table_instance)
        if existing_reservation:
            table_instance, _ = Table.objects.get_or_create(
                times=time_instance, table=str(i + 1))

    # Create a new reservation instance
    reservation = Reservation.objects.create(
        year=year_instance,
        month=month_instance,
        day=day_instance,
        time=time_instance,
        table=table_instance,
        user=request.user
    )

    # Email confirmation details
    subject = 'Reservation'
    body = f"""Hello {request.user}

Thank you for your recent booking.
Your table is reserved for {day_instance}/{month_instance}/{year_instance}
at {time_instance} {table_instance}

Kind regards,
The Savory Spot"""

    # Create an EmailMessage instance
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Setup SSL context for secure email communication
    context = ssl.create_default_context()

    # If the email receiver is not an empty string, send the email
    if not email_receiver == '':
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    # Set a flag in the session to indicate that the reservation was successful
    request.session['reserved'] = True

    # Return the reservation instance
    return reservation


def delete(request, id, email):
    # Retrieve email credentials from environment variables
    email_sender = os.environ.get("email_sender")
    email_password = os.environ.get("email_password")

    # Get the email of the user making the request
    email_receiver = request.user.email

    # Get the reservation instance using the provided id
    reservation_instance = id
    try:
        # Try to get the reservation object with the provided id
        reservation = Reservation.objects.get(id=reservation_instance)

        # Check if the user making the request is the owner of the reservation
        if request.user == reservation.user:
            # Delete the reservation
            reservation.delete()

            # Prepare email content
            subject = 'Reservation'
            body = f"""Hello {request.user}

Your reservation has been canceled.
If you did not perform this action please send us an email on our contact page.

Kind regards,
The Savory Spot"""

            # Create an EmailMessage object
            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            # Create an SSL context
            context = ssl.create_default_context()

            # Check if email is provided and the email_receiver is not empty
            if email:
                if not email_receiver == '':
                    # Connect to Gmail SMTP server and send the email
                    with smtplib.SMTP_SSL(
                      'smtp.gmail.com', 465, context=context) as smtp:
                        smtp.login(email_sender, email_password)
                        smtp.sendmail(
                            email_sender, email_receiver, em.as_string())

                    # Set a session variable to indicate successful deletion
                    request.session['deleted'] = True

    except Reservation.DoesNotExist:
        pass


class ReservationView(View):
    template_name = 'reservation.html'

    def get(self, request):
        # Get context for rendering the reservation.html template
        context = get_context(request)
        return render(request, self.template_name, context)

    def post(self, request):
        # Check if the 'submit_reservation' button was clicked
        if 'submit_reservation' in request.POST:
            # Call create function to handle reservation submission
            create(request)
        # Check if the 'delete_reservation' button was clicked
        if 'delete_reservation' in request.POST:
            # Call delete function to handle reservation deletion
            delete(request, request.POST.get('delete_reservation'), True)
        # Redirect to the 'reservation' page after processing the form
        return redirect('reservation')


class EditReservationView(View):
    template_name = 'edit_reservation.html'

    def get(self, request):
        # Get context for rendering the edit_reservation.html template
        context = get_context(request)
        return render(request, self.template_name, context)

    def post(self, request):
        # Check if 'reservation_id' is present in the form data
        if 'reservation_id' in request.POST:
            # Store the reservation_id in the session for later use
            id = request.POST.get('reservation_id')
            request.session['reservation_id'] = id
        # Check if 'edit_reservation' button was clicked
        if 'edit_reservation' in request.POST:
            # Retrieve the reservation_id from the session
            id = request.session.get('reservation_id')
            # Call create function to handle reservation update
            create(request)
            # Check if a new reservation was successfully created
            created = request.session.get('reserved')
            if created:
                # If a new reservation was created, delete the old
                delete(request, id, False)
                return redirect('reservation')
            else:
                return redirect('edit_reservation')
        # Redirect to 'edit_reservation' if no relevant buttons were clicked
        return redirect('edit_reservation')
