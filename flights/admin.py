from django.contrib import admin
from django.utils.html import format_html
from flights.models import Weather, CalendarEvent, Flight, Bus, Train, CrawlerStatus
import jdatetime
import datetime
from django.utils import timezone
import json

# -------------------- Helper Functions --------------------

def gregorian_to_jalali(dt):
    """تبدیل تاریخ میلادی به شمسی با مدیریت خطا"""
    if not dt:
        return "-"
    
    try:
        if isinstance(dt, str):
            try:
                dt = datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                dt = datetime.datetime.strptime(dt, '%Y-%m-%d')
        
        if isinstance(dt, datetime.date) and not isinstance(dt, datetime.datetime):
            dt = datetime.datetime.combine(dt, datetime.time.min)

        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())

        dt = timezone.localtime(dt)
        jalali_dt = jdatetime.datetime.fromgregorian(datetime=dt)
        return jalali_dt.strftime('%Y-%m-%d %H:%M')
    except Exception:
        return "-"

def safe_format_events(events):
    """فرمت‌بندی ایمن رویدادها با پشتیبانی از JSON و لیست"""
    if not events:
        return "بدون رویداد"
    
    try:
        if isinstance(events, str):
            try:
                events_data = json.loads(events)
                if isinstance(events_data, list):
                    return "، ".join(str(e) for e in events_data)
                return events
            except json.JSONDecodeError:
                return events
        
        if isinstance(events, dict):
            if 'مناسبت' in events:
                return events['مناسبت']
            return "، ".join(f"{k}: {v}" for k, v in events.items())
        
        if isinstance(events, list):
            return "، ".join(str(e) for e in events)
        
        return str(events)
    except Exception:
        return "خطا در نمایش رویدادها"

# -------------------- Base Admin Classes --------------------

class BaseAdmin(admin.ModelAdmin):
    """کلاس پایه برای مدل‌های ادمین"""
    list_per_page = 20

class BaseTicketAdmin(admin.ModelAdmin):
    """کلاس پایه برای مدل‌های بلیط"""
    list_per_page = 20
    
    def calendar_info(self, obj):
        if obj.calendar_event:
            events_display = safe_format_events(obj.calendar_event.events)
            is_holiday = obj.calendar_event.is_holiday
            
            return format_html(
                """
                <div style='direction: rtl; text-align: right;'>
                    <strong>تاریخ شمسی:</strong> {}<br>
                    <strong>وضعیت تعطیلی:</strong> {}<br>
                    <strong>رویدادها:</strong> {}
                </div>
                """,
                gregorian_to_jalali(obj.calendar_event.date),
                "تعطیل" if is_holiday else "غیر تعطیل",
                events_display
            )
        return "اطلاعات تقویم موجود نیست"
    calendar_info.short_description = 'اطلاعات تقویم'

    def weather_display(self, obj):
        if obj.weather:
            return format_html(
                "<div style='direction: rtl;'>"
                "<strong>دما:</strong> {}°C<br>"
                "<strong>وضعیت:</strong> {}<br>"
                "<strong>رطوبت:</strong> {}%<br>"
                "<strong>سرعت باد:</strong> {} m/s"
                "</div>",
                obj.weather.temperature,
                obj.weather.description or "-",
                obj.weather.humidity or "-",
                obj.weather.wind_speed or "-"
            )
        return "-"
    weather_display.short_description = 'آب و هوا'

    def display_departure(self, obj):
        return gregorian_to_jalali(obj.departure_datetime)
    display_departure.short_description = 'زمان حرکت'

    def display_capacity_status(self, obj):
        if obj.capacity <= 0:
            return format_html('<span style="color: red;">تکمیل شده</span>')
        return format_html('<span style="color: green;">{} صندلی خالی</span>', obj.capacity)
    display_capacity_status.short_description = 'وضعیت ظرفیت'

# -------------------- Admin Definitions --------------------

@admin.register(Flight)
class FlightAdmin(BaseTicketAdmin):
    list_display = (
        'origin', 'destination', 'type_of_class',
        'display_departure', 'display_capacity_status', 
        'price', 'weather_display', 'calendar_info'
    )
    search_fields = ('origin', 'destination', 'type_of_class')
    list_filter = ('departure_datetime', 'type_of_class')
    readonly_fields = ('weather_display', 'calendar_info', 'display_departure')

@admin.register(Bus)
class BusAdmin(BaseTicketAdmin):
    list_display = (
        'origin', 'destination', 'type_of_class',
        'display_departure', 'display_capacity_status', 'price',
        'weather_display', 'calendar_info'
    )
    search_fields = ('origin', 'destination', 'type_of_class')
    list_filter = ('departure_datetime', 'type_of_class')
    readonly_fields = ('weather_display', 'calendar_info', 'display_departure')

@admin.register(Train)
class TrainAdmin(BaseTicketAdmin):
    list_display = (
        'origin', 'destination', 'type_of_class',
        'display_departure', 'display_capacity_status', 
        'price', 'weather_display', 'calendar_info'
    )
    search_fields = ('origin', 'destination', 'type_of_class')
    list_filter = ('departure_datetime', 'type_of_class')
    readonly_fields = ('weather_display', 'calendar_info', 'display_departure')

@admin.register(Weather)
class WeatherAdmin(BaseAdmin):
    list_display = (
        'city', 'temperature', 'description',
        'humidity', 'wind_speed', 'request_date_time'
    )
    search_fields = ('city', 'description')
    list_filter = ('city',)

    def request_date_time(self, obj):
        return gregorian_to_jalali(obj.request_date_time)
    request_date_time.short_description = 'زمان درخواست'

@admin.register(CrawlerStatus)
class CrawlerStatusAdmin(BaseAdmin):
    list_display = (
        'crawler_type_display', 'last_run_formatted', 'status_display',
        'items_crawled', 'days_ahead', 'error_preview'
    )
    list_filter = ('status', 'crawler_type')
    search_fields = ('error_message',)
    readonly_fields = ('last_run', 'error_message', 'detailed_info')

    def crawler_type_display(self, obj):
        return obj.get_crawler_type_display()
    crawler_type_display.short_description = 'نوع کراولر'

    def status_display(self, obj):
        status_colors = {
            'running': 'orange',
            'completed': 'green',
            'failed': 'red',
            'pending': 'gray'
        }
        color = status_colors.get(obj.status, 'black')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 2px 6px; border-radius: 4px;">{}</span>',
            color,
            obj.get_status_display()
        )
    status_display.short_description = 'وضعیت'

    def last_run_formatted(self, obj):
        return gregorian_to_jalali(obj.last_run) if obj.last_run else '-'
    last_run_formatted.short_description = 'آخرین اجرا'

    def error_preview(self, obj):
        if obj.error_message:
            return format_html(
                '<span style="color: red; direction: rtl; display: inline-block; max-width: 200px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{}</span>',
                obj.error_message
            )
        return '-'
    error_preview.short_description = 'خطا'

    def detailed_info(self, obj):
        return format_html(
            """
            <div style="direction: rtl; padding: 10px; background: #f5f5f5; border-radius: 5px;">
                <h3>جزئیات اجرای کراولر</h3>
                <p><strong>نوع:</strong> {}</p>
                <p><strong>وضعیت:</strong> {}</p>
                <p><strong>آخرین اجرا:</strong> {}</p>
                <p><strong>تعداد آیتم‌ها:</strong> {}</p>
                <p><strong>خطا:</strong> {}</p>
            </div>
            """,
            obj.get_crawler_type_display(),
            obj.get_status_display(),
            gregorian_to_jalali(obj.last_run) if obj.last_run else 'نامشخص',
            obj.items_crawled,
            obj.error_message or 'بدون خطا'
        )
    detailed_info.short_description = 'جزئیات'

@admin.register(CalendarEvent)
class CalendarEventAdmin(BaseAdmin):
    list_display = ('date', 'display_solar_date', 'holiday_status', 'display_events')
    search_fields = ('date', 'events')
    list_filter = ('is_holiday',)
    readonly_fields = ('detailed_info',)

    def display_solar_date(self, obj):
        if obj.solar_year and obj.solar_month and obj.solar_day:
            return f"{obj.solar_year}/{obj.solar_month}/{obj.solar_day}"
        return "-"
    display_solar_date.short_description = "تاریخ شمسی"

    def holiday_status(self, obj):
        return format_html(
            '<span style="color: {};">{}</span>',
            'red' if obj.is_holiday else 'green',
            'تعطیل' if obj.is_holiday else 'غیر تعطیل'
        )
    holiday_status.short_description = "وضعیت تعطیلی"

    def display_events(self, obj):
        events = safe_format_events(obj.events)
        return format_html(
            "<div style='direction: rtl; text-align: right;'>{}</div>",
            events.replace("، ", "<br>• ")
        )
    display_events.short_description = "رویدادها"

    def detailed_info(self, obj):
        return format_html(
            """
            <div style="direction: rtl; padding: 10px; background: #f5f5f5; border-radius: 5px;">
                <h3>جزئیات رویداد</h3>
                <p><strong>تاریخ میلادی:</strong> {}</p>
                <p><strong>تاریخ شمسی:</strong> {}</p>
                <p><strong>وضعیت تعطیلی:</strong> {}</p>
                <p><strong>رویدادها:</strong> {}</p>
            </div>
            """,
            obj.date.strftime("%Y-%m-%d"),
            gregorian_to_jalali(obj.date),
            'تعطیل' if obj.is_holiday else 'غیر تعطیل',
            safe_format_events(obj.events).replace("، ", "<br>• ")
        )
    detailed_info.short_description = 'جزئیات'