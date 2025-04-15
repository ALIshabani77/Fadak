from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from utils import get_weather,get_trains,get_flights,get_buses,get_calendar_events
from datetime import datetime
from .models import Flight, Bus, Train
import logging
import jdatetime

logger = logging.getLogger(__name__)

class TravelListView(APIView):
    model_class = None
    
    def get(self, request, origin_destination, date):
        try:
            origin, destination = origin_destination.split('-')
            
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            except ValueError:
                return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, 
                              status=status.HTTP_400_BAD_REQUEST)
            
            items = None
            if self.model_class == Flight:
                items = get_flights(date, origin, destination)
            elif self.model_class == Bus:
                items = get_buses(date, origin, destination)
            elif self.model_class == Train:
                items = get_trains(date, origin, destination)
            
            if not items:
                return Response({"error": f"No {self.model_class.__name__.lower()}s found"}, 
                              status=status.HTTP_404_NOT_FOUND)
            
            items_data = []
            for item in items:
                try:
                    jalali_date = jdatetime.datetime.fromgregorian(datetime=item.departure_datetime)
                    
                    weather_data = None
                    if item.weather:
                        weather_data = {
                            'temperature': item.weather.temperature,
                            'description': item.weather.description,
                            'temp_min': item.weather.temp_min,
                            'temp_max': item.weather.temp_max,
                            'humidity': item.weather.humidity,
                            'wind_speed': item.weather.wind_speed,
                            'icon': item.weather.icon,
                            'weather_description': item.weather.weather_description,
                            'weather_icon': item.weather.weather_icon
                        }
                    
                    item_data = {
                        'id': item.id,
                        'origin': item.origin,
                        'destination': item.destination,
                        'departure_datetime': item.departure_datetime.strftime("%Y-%m-%d %H:%M"),
                        'day': jdatetime.date.j_weekdays_fa[jalali_date.weekday()],
                        'price': item.price,
                        'capacity': item.capacity,
                        'type_of_class': item.type_of_class,
                        'weather': weather_data,
                        'calendar_event': {
                            'events': item.calendar_event.events if item.calendar_event else None,
                            'is_holiday': item.calendar_event.is_holiday if item.calendar_event else False
                        }
                    }
                    items_data.append(item_data)
                except Exception as e:
                    logger.error(f"Error processing item {item.id}: {str(e)}")
                    continue
            
            return Response(items_data, status=status.HTTP_200_OK)
                
        except Exception as e:
            logger.error(f"Error in {self.__class__.__name__}: {str(e)}", exc_info=True)
            return Response({"error": "Internal server error"}, 
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class FlightList(TravelListView):
    model_class = Flight

class BusList(TravelListView):
    model_class = Bus

class TrainList(TravelListView):
    model_class = Train
        



def weather_view(request, model_name, object_id):
    """
    View for displaying destination weather information
    """
    try:
        model_mapping = {
            'flight': Flight,
            'bus': Bus,
            'train': Train
        }

        if model_name not in model_mapping:
            return JsonResponse({"error": "Invalid model name"}, status=400)

        model = model_mapping[model_name]
        obj = get_object_or_404(model, id=object_id)

        if obj.weather:
            weather_data = {
                'city': obj.weather.city,
                'temperature': obj.weather.temperature,
                'description': obj.weather.description,
                'temp_min': obj.weather.temp_min,
                'temp_max': obj.weather.temp_max,
                'humidity': obj.weather.humidity,
                'pressure': obj.weather.pressure,
                'wind_speed': obj.weather.wind_speed,
                'icon': obj.weather.icon,  # Ensure this line is correct
                'weather_description': obj.weather.weather_description,
                'weather_icon': obj.weather.weather_icon,
                'last_updated': obj.weather.request_date_time.strftime("%Y-%m-%d %H:%M")
            }
            return JsonResponse(weather_data)
        else:
            # Try to get weather if not exists
            weather = get_weather(obj.destination)
            if weather:
                obj.weather = weather
                obj.save()
                # after saving call the view again to return the weather data
                return weather_view(request, model_name, object_id)
            return JsonResponse({"error": "No weather data available"}, status=404)

    except Exception as e:
        logger.error(f"Error in weather_view: {str(e)}")
        return JsonResponse({"error": "Internal server error"}, status=500)

class CalendarEventView(APIView):
    def get(self, request, date):
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
            calendar_event = get_calendar_events(date_obj)
            
            if calendar_event:
                response_data = {
                    "date": date,
                    "is_holiday": calendar_event.is_holiday,
                    "solar_date": f"{calendar_event.solar_year}/{calendar_event.solar_month}/{calendar_event.solar_day}",
                    "events": calendar_event.events,
                }
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "No calendar events found"}, status=status.HTTP_404_NOT_FOUND)
        
        except ValueError:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error in CalendarEventView: {str(e)}")
            return Response({"error": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        





















































