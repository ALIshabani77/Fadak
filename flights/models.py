from django.db import models
from django.utils import timezone

class Flight(models.Model):
         origin = models.CharField(max_length=100)
         destination = models.CharField(max_length=100)
         time = models.CharField(max_length=50)
         price = models.CharField(max_length=50)
         capacity = models.CharField(max_length=50)
         type_of_class = models.CharField(max_length=50)
         departure_date = models.DateField()  
         request_date_time = models.DateTimeField(default=timezone.now)  
         def str(self):
             return f"{self.origin} to {self.destination} at {self.time}"

class Bus(models.Model):
         origin = models.CharField(max_length=100)
         destination = models.CharField(max_length=100)
         time = models.CharField(max_length=50)
         price = models.CharField(max_length=50)
         capacity = models.CharField(max_length=50)
         type_of_class = models.CharField(max_length=50)
         departure_date = models.DateField()  
         request_date_time = models.DateTimeField(default=timezone.now)  
         def str(self):
             return f"{self.origin} to {self.destination} at {self.time}"

class Train(models.Model):
         origin = models.CharField(max_length=100)
         destination = models.CharField(max_length=100)
         time = models.CharField(max_length=50)
         price = models.CharField(max_length=50)
         capacity = models.CharField(max_length=50)
         type_of_class = models.CharField(max_length=50)
         departure_date = models.DateField()  
         request_date_time = models.DateTimeField(default=timezone.now)  
         def str(self):
             return f"{self.origin} to {self.destination} at {self.time}"