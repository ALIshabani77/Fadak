from django.db import models
from django.utils import timezone
from django.db.models import JSONField

class CrawlerStatus(models.Model):
    CRAWLER_TYPES = (
        ('flight', 'پرواز'),
        ('train', 'قطار'),
        ('bus', 'اتوبوس'),
    )
    
    STATUS_CHOICES = (
        ('running', 'در حال اجرا'),
        ('completed', 'تکمیل شده'),
        ('failed', 'خطا'),
        ('pending', 'در انتظار'),
    )
    
    crawler_type = models.CharField(max_length=10, choices=CRAWLER_TYPES, verbose_name="نوع کراولر")
    last_run = models.DateTimeField(auto_now_add=True, verbose_name="آخرین اجرا")
    next_run = models.DateTimeField(verbose_name="اجرای بعدی")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="وضعیت")
    items_crawled = models.IntegerField(default=0, verbose_name="تعداد آیتم‌های جمع‌آوری شده")
    error_message = models.TextField(blank=True, null=True, verbose_name="پیغام خطا")
    days_ahead = models.IntegerField(default=10, verbose_name="تعداد روزهای آینده")
    
    class Meta:
        verbose_name = "وضعیت کراولر"
        verbose_name_plural = "وضعیت کراولرها"
        ordering = ['-last_run']

    def __str__(self):
        return f"{self.get_crawler_type_display()} - {self.get_status_display()}"

class CalendarEvent(models.Model):
    date = models.DateField(verbose_name="تاریخ رویداد")
    is_holiday = models.BooleanField(default=False, verbose_name="تعطیل")
    events = JSONField(blank=True, null=True, default=dict, verbose_name="رویدادها")
    solar_day = models.IntegerField(blank=True, null=True, verbose_name="روز شمسی")
    solar_month = models.IntegerField(blank=True, null=True, verbose_name="ماه شمسی")
    solar_year = models.IntegerField(blank=True, null=True, verbose_name="سال شمسی")

    class Meta:
        verbose_name = "رویداد تقویمی"
        verbose_name_plural = "رویدادهای تقویمی"

    def __str__(self):
        return f"رویداد در {self.date}"

class Weather(models.Model):
    city = models.CharField(max_length=100, verbose_name="شهر")
    temperature = models.FloatField(verbose_name="دما")
    description = models.CharField(max_length=200, blank=True, null=True, verbose_name="توضیحات آب و هوا")
    request_date_time = models.DateTimeField(auto_now_add=True, verbose_name="زمان درخواست")
    humidity = models.FloatField(blank=True, null=True, verbose_name="رطوبت")
    icon = models.CharField(max_length=50, blank=True, null=True, verbose_name="آیکون")
    pressure = models.FloatField(blank=True, null=True, verbose_name="فشار")
    temp_max = models.FloatField(blank=True, null=True, verbose_name="حداکثر دما")
    temp_min = models.FloatField(blank=True, null=True, verbose_name="حداقل دما")
    wind_speed = models.FloatField(blank=True, null=True, verbose_name="سرعت باد")

    class Meta:
        verbose_name = "آب و هوا"
        verbose_name_plural = "اطلاعات آب و هوا"

    def __str__(self):
        return f"آب و هوای {self.city} - {self.temperature}°C"

class BaseTicketModel(models.Model):
    origin = models.CharField(max_length=100, verbose_name="مبدا")
    destination = models.CharField(max_length=100, verbose_name="مقصد")
    price = models.IntegerField(verbose_name="قیمت")
    capacity = models.IntegerField(verbose_name="ظرفیت")
    type_of_class = models.CharField(max_length=50, verbose_name="نوع کلاس")
    departure_datetime = models.DateTimeField(verbose_name="تاریخ و زمان حرکت")
    request_date_time = models.DateTimeField(default=timezone.now, verbose_name="زمان درخواست")
    weather = models.ForeignKey(Weather, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="آب و هوا")
    calendar_event = models.ForeignKey(CalendarEvent, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="رویداد تقویمی")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.origin} به {self.destination} - {self.type_of_class}"

class Flight(BaseTicketModel):
    class Meta:
        verbose_name = "پرواز"
        verbose_name_plural = "پروازها"

    def __str__(self):
        return f"{self.origin} به {self.destination} - {self.type_of_class}"

class Bus(BaseTicketModel):
    amenities = JSONField(blank=True, null=True, default=list, verbose_name="امکانات")

    class Meta:
        verbose_name = "اتوبوس"
        verbose_name_plural = "اتوبوس‌ها"

    def __str__(self):
        return f"{self.origin} به {self.destination} - {self.type_of_class}"

class Train(BaseTicketModel):
    class Meta:
        verbose_name = "قطار"
        verbose_name_plural = "قطارها"

    def __str__(self):
        return f"{self.origin} به {self.destination} - {self.type_of_class}"