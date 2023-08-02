from django.shortcuts import render, redirect
from django.views import View
import smtplib
import ssl
from email.message import EmailMessage
import os
from .forms import ContactForm


class ContactView(View):
    template_name = 'contact.html'
    form_class = ContactForm

    def get(self, request):
        form = self.form_class()
        sent = request.session.get('sent', False)
        request.session.pop('sent', None)
        return render(request, self.template_name, {"form": form, "sent": sent})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            subject = 'Contact'
            body = f"""From {name}, username:{request.user}

            {message}"""

            email_sender = os.environ.get("email_sender")
            email_password = os.environ.get("email_password")
            email_receiver = os.environ.get("email_sender")

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            request.session['sent'] = True
            return redirect("contact")
        return render(request, self.template_name, {"form": form})