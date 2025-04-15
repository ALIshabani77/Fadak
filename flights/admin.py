





# from django.contrib import admin
# from .models import Flight, Bus, Train
# from .utils import gregorian_to_jalali, convert_time_to_local, get_weather  # تابع تبدیل ساعت و دریافت آب‌وهوا





# from django.utils.html import format_html

# @admin.register(Flight)
# class FlightAdmin(admin.ModelAdmin):
#     list_display = (
#         'origin', 'destination', 'capacity', 'type_of_class', 'price',
#         'display_departure_datetime', 'display_request_date_time', 'display_weather'
#     )
#     search_fields = ('origin', 'destination')
#     list_filter = ('departure_datetime', 'request_date_time')

#     def display_departure_datetime(self, obj):
#         return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
#     display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

#     def display_request_date_time(self, obj):
#         jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
#         local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
#         return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
#     display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

#     def display_weather(self, obj):
#         if obj.weather:
#             return format_html(
#                 """
#                 <table>
#                     <tr>
#                         <th>دما</th>
#                         <td>{temperature}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداقل دما</th>
#                         <td>{temp_min}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداکثر دما</th>
#                         <td>{temp_max}°C</td>
#                     </tr>
#                     <tr>
#                         <th>رطوبت</th>
#                         <td>{humidity}%</td>
#                     </tr>
#                     <tr>
#                         <th>سرعت باد</th>
#                         <td>{wind_speed} m/s</td>
#                     </tr>
#                     <tr>
#                         <th>وضعیت</th>
#                         <td>{weather_description}</td>
#                     </tr>
#                 </table>
#                 """,
#                 temperature=obj.weather.temperature,
#                 temp_min=obj.weather.temp_min,
#                 temp_max=obj.weather.temp_max,
#                 humidity=obj.weather.humidity,
#                 wind_speed=obj.weather.wind_speed,
#                 weather_description=obj.weather.weather_description
#             )
#         return "No weather data"
#     display_weather.short_description = 'Weather'  # عنوان ستون




# @admin.register(Bus)
# class BusAdmin(admin.ModelAdmin):
#     list_display = (
#         'origin', 'destination', 'capacity', 'type_of_class', 'price',
#         'display_departure_datetime', 'display_request_date_time', 'display_weather'
#     )
#     search_fields = ('origin', 'destination')
#     list_filter = ('departure_datetime', 'request_date_time')

#     def display_departure_datetime(self, obj):
#         return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
#     display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

#     def display_request_date_time(self, obj):
#         jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
#         local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
#         return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
#     display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

#     def display_weather(self, obj):
#         if obj.weather:
#             return format_html(
#                 """
#                 <table>
#                     <tr>
#                         <th>دما</th>
#                         <td>{temperature}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداقل دما</th>
#                         <td>{temp_min}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداکثر دما</th>
#                         <td>{temp_max}°C</td>
#                     </tr>
#                     <tr>
#                         <th>رطوبت</th>
#                         <td>{humidity}%</td>
#                     </tr>
#                     <tr>
#                         <th>سرعت باد</th>
#                         <td>{wind_speed} m/s</td>
#                     </tr>
#                     <tr>
#                         <th>وضعیت</th>
#                         <td>{weather_description}</td>
#                     </tr>
#                 </table>
#                 """,
#                 temperature=obj.weather.temperature,
#                 temp_min=obj.weather.temp_min,
#                 temp_max=obj.weather.temp_max,
#                 humidity=obj.weather.humidity,
#                 wind_speed=obj.weather.wind_speed,
#                 weather_description=obj.weather.weather_description
#             )
#         return "No weather data"
#     display_weather.short_description = 'Weather'  # عنوان ستون








# @admin.register(Train)
# class TrainAdmin(admin.ModelAdmin):
#     list_display = (
#         'origin', 'destination', 'capacity', 'type_of_class', 'price',
#         'display_departure_datetime', 'display_request_date_time', 'display_weather'
#     )
#     search_fields = ('origin', 'destination')
#     list_filter = ('departure_datetime', 'request_date_time')

#     def display_departure_datetime(self, obj):
#         return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
#     display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

#     def display_request_date_time(self, obj):
#         jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
#         local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
#         return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
#     display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

#     def display_weather(self, obj):
#         if obj.weather:
#             return format_html(
#                 """
#                 <table>
#                     <tr>
#                         <th>دما</th>
#                         <td>{temperature}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداقل دما</th>
#                         <td>{temp_min}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداکثر دما</th>
#                         <td>{temp_max}°C</td>
#                     </tr>
#                     <tr>
#                         <th>رطوبت</th>
#                         <td>{humidity}%</td>
#                     </tr>
#                     <tr>
#                         <th>سرعت باد</th>
#                         <td>{wind_speed} m/s</td>
#                     </tr>
#                     <tr>
#                         <th>وضعیت</th>
#                         <td>{weather_description}</td>
#                     </tr>
#                 </table>
#                 """,
#                 temperature=obj.weather.temperature,
#                 temp_min=obj.weather.temp_min,
#                 temp_max=obj.weather.temp_max,
#                 humidity=obj.weather.humidity,
#                 wind_speed=obj.weather.wind_speed,
#                 weather_description=obj.weather.weather_description
#             )
#         return "No weather data"
#     display_weather.short_description = 'Weather'  # عنوان ستون






# from django.contrib import admin
# from .models import Weather
# from django.utils.html import format_html
# from .utils import gregorian_to_jalali, convert_time_to_local

# @admin.register(Weather)
# class WeatherAdmin(admin.ModelAdmin):
#     list_display = (
#         'city', 'display_temperature', 'display_temp_min', 'display_temp_max', 
#         'display_humidity', 'display_pressure', 'display_wind_speed', 
#         'display_weather_description', 'display_request_date_time'
#     )
#     search_fields = ('city',)
#     list_filter = ('request_date_time',)

#     def display_temperature(self, obj):
#         return f"{obj.temperature}°C"
#     display_temperature.short_description = 'Temperature'

#     def display_temp_min(self, obj):
#         return f"{obj.temp_min}°C"
#     display_temp_min.short_description = 'Min Temperature'

#     def display_temp_max(self, obj):
#         return f"{obj.temp_max}°C"
#     display_temp_max.short_description = 'Max Temperature'

#     def display_humidity(self, obj):
#         return f"{obj.humidity}%"
#     display_humidity.short_description = 'Humidity'

#     def display_pressure(self, obj):
#         return f"{obj.pressure} hPa"
#     display_pressure.short_description = 'Pressure'

#     def display_wind_speed(self, obj):
#         return f"{obj.wind_speed} m/s"
#     display_wind_speed.short_description = 'Wind Speed'

#     def display_weather_description(self, obj):
#         return obj.weather_description
#     display_weather_description.short_description = 'Weather Description'

#     def display_request_date_time(self, obj):
#         jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
#         local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
#         return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
#     display_request_date_time.short_description = 'Request DateTime'












from django.contrib import admin
from .models import Flight, Bus, Train, Weather, CalendarEvent
from .utils import gregorian_to_jalali, convert_time_to_local
from django.utils.html import format_html

# @admin.register(Flight)
# class FlightAdmin(admin.ModelAdmin):
#     list_display = (
#         'origin', 'destination', 'capacity', 'type_of_class', 'price',
#         'display_departure_datetime', 'display_request_date_time', 'display_weather', 'display_calendar_event'
#     )
#     search_fields = ('origin', 'destination')
#     list_filter = ('departure_datetime', 'request_date_time')

#     def display_departure_datetime(self, obj):
#         return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
#     display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

#     def display_request_date_time(self, obj):
#         jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
#         local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
#         return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
#     display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

#     def display_weather(self, obj):
#         if obj.weather:
#             return format_html(
#                 """
#                 <table>
#                     <tr>
#                         <th>دما</th>
#                         <td>{temperature}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداقل دما</th>
#                         <td>{temp_min}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداکثر دما</th>
#                         <td>{temp_max}°C</td>
#                     </tr>
#                     <tr>
#                         <th>رطوبت</th>
#                         <td>{humidity}%</td>
#                     </tr>
#                     <tr>
#                         <th>سرعت باد</th>
#                         <td>{wind_speed} m/s</td>
#                     </tr>
#                     <tr>
#                         <th>وضعیت</th>
#                         <td>{weather_description}</td>
#                     </tr>
#                 </table>
#                 """,
#                 temperature=obj.weather.temperature,
#                 temp_min=obj.weather.temp_min,
#                 temp_max=obj.weather.temp_max,
#                 humidity=obj.weather.humidity,
#                 wind_speed=obj.weather.wind_speed,
#                 weather_description=obj.weather.weather_description
#             )
#         return "No weather data"
#     display_weather.short_description = 'Weather'  # عنوان ستون

#     def display_calendar_event(self, obj):
#         if obj.calendar_event:
#             return f"{obj.calendar_event.solar_event} (تعطیل: {'بله' if obj.calendar_event.is_holiday else 'خیر'})"
#         return "No calendar event"
#     display_calendar_event.short_description = 'رویداد تقویم'  # عنوان ستون

# @admin.register(Bus)
# class BusAdmin(admin.ModelAdmin):
#     list_display = (
#         'origin', 'destination', 'capacity', 'type_of_class', 'price',
#         'display_departure_datetime', 'display_request_date_time', 'display_weather', 'display_calendar_event'
#     )
#     search_fields = ('origin', 'destination')
#     list_filter = ('departure_datetime', 'request_date_time')

#     def display_departure_datetime(self, obj):
#         return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
#     display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

#     def display_request_date_time(self, obj):
#         jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
#         local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
#         return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
#     display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

#     def display_weather(self, obj):
#         if obj.weather:
#             return format_html(
#                 """
#                 <table>
#                     <tr>
#                         <th>دما</th>
#                         <td>{temperature}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداقل دما</th>
#                         <td>{temp_min}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداکثر دما</th>
#                         <td>{temp_max}°C</td>
#                     </tr>
#                     <tr>
#                         <th>رطوبت</th>
#                         <td>{humidity}%</td>
#                     </tr>
#                     <tr>
#                         <th>سرعت باد</th>
#                         <td>{wind_speed} m/s</td>
#                     </tr>
#                     <tr>
#                         <th>وضعیت</th>
#                         <td>{weather_description}</td>
#                     </tr>
#                 </table>
#                 """,
#                 temperature=obj.weather.temperature,
#                 temp_min=obj.weather.temp_min,
#                 temp_max=obj.weather.temp_max,
#                 humidity=obj.weather.humidity,
#                 wind_speed=obj.weather.wind_speed,
#                 weather_description=obj.weather.weather_description
#             )
#         return "No weather data"
#     display_weather.short_description = 'Weather'  # عنوان ستون

#     def display_calendar_event(self, obj):
#         if obj.calendar_event:
#             return f"{obj.calendar_event.solar_event} (تعطیل: {'بله' if obj.calendar_event.is_holiday else 'خیر'})"
#         return "No calendar event"
#     display_calendar_event.short_description = 'رویداد تقویم'  # عنوان ستون

# @admin.register(Train)
# class TrainAdmin(admin.ModelAdmin):
#     list_display = (
#         'origin', 'destination', 'capacity', 'type_of_class', 'price',
#         'display_departure_datetime', 'display_request_date_time', 'display_weather', 'display_calendar_event'
#     )
#     search_fields = ('origin', 'destination')
#     list_filter = ('departure_datetime', 'request_date_time')

#     def display_departure_datetime(self, obj):
#         return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
#     display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

#     def display_request_date_time(self, obj):
#         jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
#         local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
#         return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
#     display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

#     def display_weather(self, obj):
#         if obj.weather:
#             return format_html(
#                 """
#                 <table>
#                     <tr>
#                         <th>دما</th>
#                         <td>{temperature}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداقل دما</th>
#                         <td>{temp_min}°C</td>
#                     </tr>
#                     <tr>
#                         <th>حداکثر دما</th>
#                         <td>{temp_max}°C</td>
#                     </tr>
#                     <tr>
#                         <th>رطوبت</th>
#                         <td>{humidity}%</td>
#                     </tr>
#                     <tr>
#                         <th>سرعت باد</th>
#                         <td>{wind_speed} m/s</td>
#                     </tr>
#                     <tr>
#                         <th>وضعیت</th>
#                         <td>{weather_description}</td>
#                     </tr>
#                 </table>
#                 """,
#                 temperature=obj.weather.temperature,
#                 temp_min=obj.weather.temp_min,
#                 temp_max=obj.weather.temp_max,
#                 humidity=obj.weather.humidity,
#                 wind_speed=obj.weather.wind_speed,
#                 weather_description=obj.weather.weather_description
#             )
#         return "No weather data"
#     display_weather.short_description = 'Weather'  # عنوان ستون

#     def display_calendar_event(self, obj):
#         if obj.calendar_event:
#             return f"{obj.calendar_event.solar_event} (تعطیل: {'بله' if obj.calendar_event.is_holiday else 'خیر'})"
#         return "No calendar event"
#     display_calendar_event.short_description = 'رویداد تقویم'  # عنوان ستون
from django.contrib import admin
from .models import Flight, Bus, Train, CalendarEvent, Weather
from .utils import gregorian_to_jalali, convert_time_to_local
from django.utils.html import format_html

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'origin', 'destination', 'capacity', 'type_of_class', 'price',
        'display_departure_datetime', 'display_request_date_time', 'display_weather', 'display_calendar_events'
    )
    search_fields = ('origin', 'destination')
    list_filter = ('departure_datetime', 'request_date_time')

    def display_departure_datetime(self, obj):
        return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
    display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

    def display_request_date_time(self, obj):
        jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
        local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
        return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
    display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

    def display_weather(self, obj):
        if obj.weather:
            return format_html(
                """
                <table>
                    <tr>
                        <th>دما</th>
                        <td>{temperature}°C</td>
                    </tr>
                    <tr>
                        <th>حداقل دما</th>
                        <td>{temp_min}°C</td>
                    </tr>
                    <tr>
                        <th>حداکثر دما</th>
                        <td>{temp_max}°C</td>
                    </tr>
                    <tr>
                        <th>رطوبت</th>
                        <td>{humidity}%</td>
                    </tr>
                    <tr>
                        <th>سرعت باد</th>
                        <td>{wind_speed} m/s</td>
                    </tr>
                    <tr>
                        <th>وضعیت</th>
                        <td>{weather_description}</td>
                    </tr>
                </table>
                """,
                temperature=obj.weather.temperature,
                temp_min=obj.weather.temp_min,
                temp_max=obj.weather.temp_max,
                humidity=obj.weather.humidity,
                wind_speed=obj.weather.wind_speed,
                weather_description=obj.weather.weather_description
            )
        return "No weather data"
    display_weather.short_description = 'Weather'  # عنوان ستون

    def display_calendar_events(self, obj):
        if obj.calendar_event:
            return obj.calendar_event.events if obj.calendar_event.events else "No events"
        return "No calendar event"
    display_calendar_events.short_description = 'مناسبت‌ها'  # عنوان ستون

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = (
        'origin', 'destination', 'capacity', 'type_of_class', 'price',
        'display_departure_datetime', 'display_request_date_time', 'display_weather', 'display_calendar_events'
    )
    search_fields = ('origin', 'destination')
    list_filter = ('departure_datetime', 'request_date_time')

    def display_departure_datetime(self, obj):
        return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
    display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

    def display_request_date_time(self, obj):
        jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
        local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
        return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
    display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

    def display_weather(self, obj):
        if obj.weather:
            return format_html(
                """
                <table>
                    <tr>
                        <th>دما</th>
                        <td>{temperature}°C</td>
                    </tr>
                    <tr>
                        <th>حداقل دما</th>
                        <td>{temp_min}°C</td>
                    </tr>
                    <tr>
                        <th>حداکثر دما</th>
                        <td>{temp_max}°C</td>
                    </tr>
                    <tr>
                        <th>رطوبت</th>
                        <td>{humidity}%</td>
                    </tr>
                    <tr>
                        <th>سرعت باد</th>
                        <td>{wind_speed} m/s</td>
                    </tr>
                    <tr>
                        <th>وضعیت</th>
                        <td>{weather_description}</td>
                    </tr>
                </table>
                """,
                temperature=obj.weather.temperature,
                temp_min=obj.weather.temp_min,
                temp_max=obj.weather.temp_max,
                humidity=obj.weather.humidity,
                wind_speed=obj.weather.wind_speed,
                weather_description=obj.weather.weather_description
            )
        return "No weather data"
    display_weather.short_description = 'Weather'  # عنوان ستون

    def display_calendar_events(self, obj):
        if obj.calendar_event:
            return obj.calendar_event.events if obj.calendar_event.events else "No events"
        return "No calendar event"
    display_calendar_events.short_description = 'مناسبت‌ها'  # عنوان ستون

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = (
        'origin', 'destination', 'capacity', 'type_of_class', 'price',
        'display_departure_datetime', 'display_request_date_time', 'display_weather', 'display_calendar_events'
    )
    search_fields = ('origin', 'destination')
    list_filter = ('departure_datetime', 'request_date_time')

    def display_departure_datetime(self, obj):
        return obj.departure_datetime.strftime("%Y-%m-%d %H:%M")  # تاریخ میلادی
    display_departure_datetime.short_description = 'Departure DateTime'  # عنوان ستون

    def display_request_date_time(self, obj):
        jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
        local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
        return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
    display_request_date_time.short_description = 'Request DateTime'  # عنوان ستون

    def display_weather(self, obj):
        if obj.weather:
            return format_html(
                """
                <table>
                    <tr>
                        <th>دما</th>
                        <td>{temperature}°C</td>
                    </tr>
                    <tr>
                        <th>حداقل دما</th>
                        <td>{temp_min}°C</td>
                    </tr>
                    <tr>
                        <th>حداکثر دما</th>
                        <td>{temp_max}°C</td>
                    </tr>
                    <tr>
                        <th>رطوبت</th>
                        <td>{humidity}%</td>
                    </tr>
                    <tr>
                        <th>سرعت باد</th>
                        <td>{wind_speed} m/s</td>
                    </tr>
                    <tr>
                        <th>وضعیت</th>
                        <td>{weather_description}</td>
                    </tr>
                </table>
                """,
                temperature=obj.weather.temperature,
                temp_min=obj.weather.temp_min,
                temp_max=obj.weather.temp_max,
                humidity=obj.weather.humidity,
                wind_speed=obj.weather.wind_speed,
                weather_description=obj.weather.weather_description
            )
        return "No weather data"
    display_weather.short_description = 'Weather'  # عنوان ستون

    def display_calendar_events(self, obj):
        if obj.calendar_event:
            return obj.calendar_event.events if obj.calendar_event.events else "No events"
        return "No calendar event"
    display_calendar_events.short_description = 'مناسبت‌ها'  # عنوان ستون

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = (
        'city', 'display_temperature', 'display_temp_min', 'display_temp_max', 
        'display_humidity', 'display_pressure', 'display_wind_speed', 
        'display_weather_description', 'display_request_date_time'
    )
    search_fields = ('city',)
    list_filter = ('request_date_time',)

    def display_temperature(self, obj):
        return f"{obj.temperature}°C"
    display_temperature.short_description = 'Temperature'

    def display_temp_min(self, obj):
        return f"{obj.temp_min}°C"
    display_temp_min.short_description = 'Min Temperature'

    def display_temp_max(self, obj):
        return f"{obj.temp_max}°C"
    display_temp_max.short_description = 'Max Temperature'

    def display_humidity(self, obj):
        return f"{obj.humidity}%"
    display_humidity.short_description = 'Humidity'

    def display_pressure(self, obj):
        return f"{obj.pressure} hPa"
    display_pressure.short_description = 'Pressure'

    def display_wind_speed(self, obj):
        return f"{obj.wind_speed} m/s"
    display_wind_speed.short_description = 'Wind Speed'

    def display_weather_description(self, obj):
        return obj.weather_description
    display_weather_description.short_description = 'Weather Description'

    def display_request_date_time(self, obj):
        jalali_date = gregorian_to_jalali(obj.request_date_time).split()[0]  # فقط تاریخ شمسی
        local_time = convert_time_to_local(obj.request_date_time)  # فقط ساعت محلی
        return f"{jalali_date} {local_time}"  # ترکیب تاریخ شمسی و ساعت محلی
    display_request_date_time.short_description = 'Request DateTime'

# from django.contrib import admin
# from .models import CalendarEvent
# from django.utils.html import format_html

# @admin.register(CalendarEvent)
# class CalendarEventAdmin(admin.ModelAdmin):
#     list_display = (
#         'date', 'is_holiday', 'display_solar_date', 'display_moon_date', 
#         'display_gregorian_date', 'display_events'
#     )
#     search_fields = ('date', 'events')
#     list_filter = ('is_holiday', 'solar_year', 'moon_year', 'gregorian_year')

#     def display_solar_date(self, obj):
#         return f"{obj.solar_year}/{obj.solar_month}/{obj.solar_day} ({obj.solar_day_week})"
#     display_solar_date.short_description = 'تاریخ شمسی'

#     def display_moon_date(self, obj):
#         return f"{obj.moon_year}/{obj.moon_month}/{obj.moon_day} ({obj.moon_day_week})"
#     display_moon_date.short_description = 'تاریخ قمری'

#     def display_gregorian_date(self, obj):
#         return f"{obj.gregorian_year}/{obj.gregorian_month}/{obj.gregorian_day} ({obj.gregorian_day_week})"
#     display_gregorian_date.short_description = 'تاریخ میلادی'

#     def display_events(self, obj):
#         return obj.events if obj.events else "No events"
#     display_events.short_description = 'مناسبت‌ها'


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = (
        'display_jalali_date', 'is_holiday', 'display_solar_date', 
        'display_moon_date', 'display_gregorian_date', 'display_events'
    )
    search_fields = ('date', 'events')
    list_filter = ('is_holiday', 'solar_year', 'moon_year', 'gregorian_year')

    def display_jalali_date(self, obj):
        return gregorian_to_jalali(obj.date).split()[0]  # فقط تاریخ شمسی
    display_jalali_date.short_description = 'date'
    display_jalali_date.admin_order_field = 'date'  # امکان مرتب سازی بر اساس این فیلد

    def display_solar_date(self, obj):
        return f"{obj.solar_year}/{obj.solar_month}/{obj.solar_day} ({obj.solar_day_week})"
    display_solar_date.short_description = 'تاریخ شمسی'

    def display_moon_date(self, obj):
        return f"{obj.moon_year}/{obj.moon_month}/{obj.moon_day} ({obj.moon_day_week})"
    display_moon_date.short_description = 'تاریخ قمری'

    def display_gregorian_date(self, obj):
        return f"{obj.gregorian_year}/{obj.gregorian_month}/{obj.gregorian_day} ({obj.gregorian_day_week})"
    display_gregorian_date.short_description = 'تاریخ میلادی'

    def display_events(self, obj):
        return obj.events if obj.events else "No events"
    display_events.short_description = 'مناسبت‌ها'












































