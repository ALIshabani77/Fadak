from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import get_flights  

class FlightList(APIView):
         def get(self, request, origin_destination, date):  
            
             origin, destination = origin_destination.split('-')
             
             flights_json = get_flights(date, origin, destination)

             if flights_json:
                 return Response(flights_json, content_type='application/json')
             else:
                 return Response({"error": "No flights found"}, status=status.HTTP_404_NOT_FOUND)
             