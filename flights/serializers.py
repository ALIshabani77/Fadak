from rest_framework import serializers
from .models import Flight, Bus, Train, Weather, CalendarEvent

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['city', 'temperature', 'description', 'humidity', 'wind_speed', 'icon']

class CalendarEventSerializer(serializers.ModelSerializer):
    solar_date = serializers.SerializerMethodField()
    
    class Meta:
        model = CalendarEvent
        fields = ['is_holiday', 'solar_date', 'events']
    
    def get_solar_date(self, obj):
        return f"{obj.solar_year}/{obj.solar_month}/{obj.solar_day}"

class TravelSerializer(serializers.ModelSerializer):
    jalali_date = serializers.SerializerMethodField()
    day = serializers.SerializerMethodField()
    weather = WeatherSerializer(read_only=True)
    calendar_event = CalendarEventSerializer(read_only=True)
    
    class Meta:
        fields = [
            'id', 'origin', 'destination', 'departure_datetime', 
            'jalali_date', 'day', 'price', 'capacity', 'type_of_class',
            'weather', 'calendar_event'
        ]
    
    def get_jalali_date(self, obj):
        return obj.jalali_date
    
    def get_day(self, obj):
        return obj.day

class FlightSerializer(TravelSerializer):
    class Meta(TravelSerializer.Meta):
        model = Flight
        fields = TravelSerializer.Meta.fields + ['flight_number', 'airline']

class BusSerializer(TravelSerializer):
    class Meta(TravelSerializer.Meta):
        model = Bus
        fields = TravelSerializer.Meta.fields + ['bus_company']

class TrainSerializer(TravelSerializer):
    class Meta(TravelSerializer.Meta):
        model = Train
        fields = TravelSerializer.Meta.fields + ['train_number']