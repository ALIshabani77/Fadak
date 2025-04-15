
# from django.db import models
# from django.utils import timezone


# class Weather(models.Model):
#     city = models.CharField(max_length=100)  # نام شهر
#     temperature = models.FloatField()  # دمای فعلی
#     temp_min = models.FloatField()  # حداقل دما
#     temp_max = models.FloatField()  # حداکثر دما
#     humidity = models.FloatField()  # رطوبت
#     pressure = models.FloatField()  # فشار هوا
#     wind_speed = models.FloatField()  # سرعت باد
#     weather_description = models.CharField(max_length=200)  # توضیحات آب‌وهوا
#     weather_icon = models.CharField(max_length=20)  # آیکون آب‌وهوا
#     request_date_time = models.DateTimeField(auto_now_add=True)  # زمان درخواست

#     def str(self):
#         return f"Weather for {self.city} at {self.request_date_time}"



# class Flight(models.Model):
#     origin = models.CharField(max_length=100)
#     destination = models.CharField(max_length=100)
#     price = models.IntegerField()
#     capacity = models.IntegerField()
#     type_of_class = models.CharField(max_length=50)
#     departure_datetime = models.DateTimeField()
#     request_date_time = models.DateTimeField(default=timezone.now)
#     weather = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True, blank=True)  # ارتباط با مدل Weather

#     def str(self):
#         return f"{self.origin} to {self.destination} at {self.departure_datetime}"

# class Bus(models.Model):
#     origin = models.CharField(max_length=100)
#     destination = models.CharField(max_length=100)
#     price = models.IntegerField()
#     capacity = models.IntegerField()
#     type_of_class = models.CharField(max_length=50)
#     departure_datetime = models.DateTimeField()
#     request_date_time = models.DateTimeField(default=timezone.now)
#     weather = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True, blank=True)  # ارتباط با مدل Weather

#     def str(self):
#         return f"{self.origin} to {self.destination} at {self.departure_datetime}"

# class Train(models.Model):
#     origin = models.CharField(max_length=100)
#     destination = models.CharField(max_length=100)
#     price = models.IntegerField()
#     capacity = models.IntegerField()
#     type_of_class = models.CharField(max_length=50)
#     departure_datetime = models.DateTimeField()
#     request_date_time = models.DateTimeField(default=timezone.now)
#     weather = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True, blank=True)  # ارتباط با مدل Weather

#     def str(self):
#         return f"{self.origin} to {self.destination} at {self.departure_datetime}"





# class CalendarEvent(models.Model):
#     date = models.DateField(unique=True)  # تاریخ شمسی
#     solar_events = models.TextField(blank=True, null=True)  # مناسبت‌های شمسی
#     lunar_events = models.TextField(blank=True, null=True)  # مناسبت‌های قمری
#     is_holiday = models.BooleanField(default=False)  # تعطیل بودن یا نبودن
#     request_date_time = models.DateTimeField(auto_now_add=True)  # زمان درخواست

#     def str(self):
#         return f"Calendar Event for {self.date}"
    







from django.db import models
from django.utils import timezone

# class CalendarEvent(models.Model):
#     date = models.DateField()  # تاریخ رویداد
#     is_holiday = models.BooleanField(default=False)  # تعطیل بودن یا نبودن
#     solar_day = models.IntegerField(null=True, blank=True)  # روز شمسی
#     solar_month = models.IntegerField(null=True, blank=True)  # ماه شمسی
#     solar_year = models.IntegerField(null=True, blank=True)  # سال شمسی
#     solar_day_week = models.CharField(max_length=10, blank=True, null=True)  # روز هفته شمسی
#     moon_day = models.IntegerField(null=True, blank=True)  # روز قمری
#     moon_month = models.IntegerField(null=True, blank=True)  # ماه قمری
#     moon_year = models.IntegerField(null=True, blank=True)  # سال قمری
#     moon_day_week = models.CharField(max_length=10, blank=True, null=True)  # روز هفته قمری
#     gregorian_day = models.IntegerField(null=True, blank=True)  # روز میلادی
#     gregorian_month = models.IntegerField(default=0)  # ماه میلادی
#     gregorian_year = models.IntegerField(default=0)  # سال میلادی
#     gregorian_day_week = models.CharField(max_length=10, blank=True, null=True)  # روز هفته میلادی
#     events = models.TextField(blank=True, null=True, default="")  # مناسبت‌ها (شمسی و قمری ترکیبی)
#     #events = models.JSONField(blank=True, null=True, default="")
    
#     def __str__(self):
#         return f"Calendar Event on {self.date}"

#     class Meta:
#         verbose_name = "Calendar Event"
#         verbose_name_plural = "Calendar Events"



from django.db import models
from django.contrib.postgres.fields import JSONField  # برای Django < 3.1
# از Django 3.1 به بعد:
from django.db.models import JSONField

class CalendarEvent(models.Model):
    date = models.DateField()  # تاریخ رویداد
    is_holiday = models.BooleanField(default=False)  # تعطیل بودن یا نبودن
    solar_day = models.IntegerField(null=True, blank=True)  # روز شمسی
    solar_month = models.IntegerField(null=True, blank=True)  # ماه شمسی
    solar_year = models.IntegerField(null=True, blank=True)  # سال شمسی
    solar_day_week = models.CharField(max_length=10, blank=True, null=True)  # روز هفته شمسی
    moon_day = models.IntegerField(null=True, blank=True)  # روز قمری
    moon_month = models.IntegerField(null=True, blank=True)  # ماه قمری
    moon_year = models.IntegerField(null=True, blank=True)  # سال قمری
    moon_day_week = models.CharField(max_length=10, blank=True, null=True)  # روز هفته قمری
    gregorian_day = models.IntegerField(null=True, blank=True)  # روز میلادی
    gregorian_month = models.IntegerField(default=0)  # ماه میلادی
    gregorian_year = models.IntegerField(default=0)  # سال میلادی
    gregorian_day_week = models.CharField(max_length=10, blank=True, null=True)  # روز هفته میلادی
    
    # تغییر این قسمت به JSONField با مقدار پیش‌فرض callable
    events = JSONField(blank=True, null=True, default=dict)  # استفاده از dict به عنوان callable
    
    def __str__(self):
        return f"Calendar Event on {self.date}"

    class Meta:
        verbose_name = "Calendar Event"
        verbose_name_plural = "Calendar Events"
    
class Weather(models.Model):
    city = models.CharField(max_length=100, verbose_name="شهر")
    temperature = models.FloatField(verbose_name="دما")
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name="توضیحات")
    temp_min = models.FloatField(null=True, blank=True, verbose_name="حداقل دما")
    temp_max = models.FloatField(null=True, blank=True, verbose_name="حداکثر دما")
    humidity = models.FloatField(null=True, blank=True, verbose_name="رطوبت")
    pressure = models.FloatField(null=True, blank=True, verbose_name="فشار هوا")
    wind_speed = models.FloatField(null=True, blank=True, verbose_name="سرعت باد")
    icon = models.CharField(max_length=20, blank=True, null=True, verbose_name="آیکون")
    weather_description = models.CharField(max_length=200, blank=True, null=True, verbose_name="توضیحات آب و هوا")
    weather_icon = models.CharField(max_length=20, blank=True, null=True, verbose_name="آیکون آب و هوا")
    request_date_time = models.DateTimeField(auto_now_add=True, verbose_name="زمان درخواست")

    class Meta:
        verbose_name = "آب و هوا"
        verbose_name_plural = "اطلاعات آب و هوا"

    def __str__(self):
        return f"آب و هوای {self.city} در تاریخ {self.request_date_time}"



class Flight(models.Model):
    origin = models.CharField(max_length=100)  # مبدا
    destination = models.CharField(max_length=100)  # مقصد
    price = models.IntegerField()  # قیمت
    capacity = models.IntegerField()  # ظرفیت
    type_of_class = models.CharField(max_length=50)  # نوع کلاس
    departure_datetime = models.DateTimeField()  # تاریخ و زمان حرکت
    request_date_time = models.DateTimeField(default=timezone.now)  # تاریخ و زمان درخواست
    weather = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True, blank=True)  # آب‌وهوا
    calendar_event = models.ForeignKey(CalendarEvent, on_delete=models.SET_NULL, null=True, blank=True)  # رویداد تقویم

    def __str__(self):
        return f"{self.origin} to {self.destination} at {self.departure_datetime}"


class Bus(models.Model):
    origin = models.CharField(max_length=100)  # مبدا
    destination = models.CharField(max_length=100)  # مقصد
    price = models.IntegerField()  # قیمت
    capacity = models.IntegerField()  # ظرفیت
    type_of_class = models.CharField(max_length=50)  # نوع کلاس
    departure_datetime = models.DateTimeField()  # تاریخ و زمان حرکت
    request_date_time = models.DateTimeField(default=timezone.now)  # تاریخ و زمان درخواست
    weather = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True, blank=True)  # آب‌وهوا
    calendar_event = models.ForeignKey(CalendarEvent, on_delete=models.SET_NULL, null=True, blank=True)  # رویداد تقویم

    def __str__(self):
        return f"{self.origin} to {self.destination} at {self.departure_datetime}"
    


class Train(models.Model):
    origin = models.CharField(max_length=100)  # مبدا
    destination = models.CharField(max_length=100)  # مقصد
    price = models.IntegerField()  # قیمت
    capacity = models.IntegerField()  # ظرفیت
    type_of_class = models.CharField(max_length=50)  # نوع کلاس
    departure_datetime = models.DateTimeField()  # تاریخ و زمان حرکت
    request_date_time = models.DateTimeField(default=timezone.now)  # تاریخ و زمان درخواست
    weather = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True, blank=True)  # آب‌وهوا
    calendar_event = models.ForeignKey(CalendarEvent, on_delete=models.SET_NULL, null=True, blank=True)  # رویداد تقویم

    def __str__(self):
        return f"{self.origin} to {self.destination} at {self.departure_datetime}" 
