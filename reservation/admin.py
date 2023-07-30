from django.contrib import admin
from .models import  Month, Day, Time, Table, Reservation

admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Time)
admin.site.register(Table)
admin.site.register(Reservation)
