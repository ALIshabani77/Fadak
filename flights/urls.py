from django.urls import path
from .views import FlightList
from .views import Buslist
from .views import Trainlist


urlpatterns = [

         path('api/flights/<str:origin_destination>/<str:date>/', FlightList.as_view(), name='flight_list'),
         path('api/buses/<str:origin_destination>/<str:date>/', Buslist.as_view(), name='bus_list'), 
         path('api/trains/<str:origin_destination>/<str:date>/', Trainlist.as_view(), name='train_list'), 
         
              ]



