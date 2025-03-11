from django.contrib import admin
from .models import Flight, Bus, Train  

    
@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
         list_display = ('origin', 'destination', 'time', 'price', 'capacity', 'type_of_class', 'departure_date', 'request_date_time')
         search_fields = ('origin', 'destination')
         list_filter = ('departure_date', 'request_date_time')

     
@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
         list_display = ('origin', 'destination', 'time', 'price', 'capacity', 'type_of_class', 'departure_date', 'request_date_time')
         search_fields = ('origin', 'destination')
         list_filter = ('departure_date', 'request_date_time')

    
@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
         list_display = ('origin', 'destination', 'time', 'price', 'capacity', 'type_of_class', 'departure_date', 'request_date_time')
         search_fields = ('origin', 'destination')
         list_filter = ('departure_date', 'request_date_time')