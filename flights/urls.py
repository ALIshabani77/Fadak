from django.urls import path
from .views import FlightList
from .views import BusList
from .views import TrainList


urlpatterns = [

         path('api/flights/<str:origin_destination>/<str:date>/', FlightList.as_view(), name='flight_list'),
         path('api/buses/<str:origin_destination>/<str:date>/', BusList.as_view(), name='bus_list'), 
         path('api/trains/<str:origin_destination>/<str:date>/', TrainList.as_view(), name='train_list'), 
         
              ]



