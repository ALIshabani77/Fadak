from django.urls import path
from .views import FlightList
from .views import BusList
from .views import TrainList


from django.contrib import admin
from django.urls import path
from flights.views import FlightList, BusList, TrainList, CrawlerStatusView
from django.urls import include


urlpatterns = [
        # path('admin/', admin.site.urls),
         path('api/flights/<str:origin_destination>/<str:date>/', FlightList.as_view(), name='flight_list'),
         path('api/buses/<str:origin_destination>/<str:date>/', BusList.as_view(), name='bus_list'), 
         path('api/trains/<str:origin_destination>/<str:date>/', TrainList.as_view(), name='train_list'), 
         path('api/crawler-status/', CrawlerStatusView.as_view(), name='crawler-status'),
         
              ]




