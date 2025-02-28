from django.urls import path
from .views import FlightList

urlpatterns = [
         path('api/flights/<str:origin_destination>/<str:date>/', FlightList.as_view(), name='flight_list'),
     ]



