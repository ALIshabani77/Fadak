from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_flights  
from .utils import get_bus
from .utils import get_trains

class FlightList(APIView):
         def get(self, request, origin_destination, date):  
            
             origin, destination = origin_destination.split('-')
             
             flights = get_flights(date, origin, destination)

             if flights:
                 return Response(flights, content_type='application/json')
                 #flights_data = json.loads(flights_json)  # تبدیل رشته JSON به دیکشنری
                 #return Response(flights_data, content_type='application/json')
             else:
                 return Response({"error": "No flights found"}, status=status.HTTP_404_NOT_FOUND)
             



        
             


class Buslist(APIView):
    def get(self, request, origin_destination, date):

        origin, destination=origin_destination.split('-')

        buses_json=get_bus(origin,destination,date)

        if buses_json:
             return Response(buses_json, content_type='application/json')
             #buses_data = json.loads(buses_json)  # تبدیل رشته JSON به دیکشنری
             #return Response(buses_data, content_type='application/json')
        else:
            return Response({"error": "No flights found"}, status=status.HTTP_404_NOT_FOUND)
        

        



class Trainlist(APIView):
    def get(self, request, origin_destination, date):

        origin, destination=origin_destination.split('-')

        trains_json=get_trains(origin,destination,date)

        if trains_json:
             return Response(trains_json, content_type='application/json')
             #buses_data = json.loads(buses_json)  # تبدیل رشته JSON به دیکشنری
             #return Response(buses_data, content_type='application/json')
        else:
            return Response({"error": "No flights found"}, status=status.HTTP_404_NOT_FOUND)
        
             



