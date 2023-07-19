from django.shortcuts import render
from django.views import View


class ContactView(View):
    template_name = 'contact.html'

    def get(self, request):

        return render(request, self.template_name)
