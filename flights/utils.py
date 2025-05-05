import re
import time
from datetime import datetime
from django.utils import timezone
from django.conf import settings
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from .models import Weather, CalendarEvent, Flight, Bus, Train
import logging
import jdatetime

logger = logging.getLogger(__name__)

# -------------------- Helper Functions --------------------

def gregorian_to_jalali(dt):
    """Convert Gregorian datetime to Jalali date string"""
    if isinstance(dt, str):
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')
        dt = timezone.make_aware(dt)
    
    jalali_dt = jdatetime.datetime.fromgregorian(datetime=dt)
    return jalali_dt.strftime('%Y-%m-%d %H:%M')

def convert_time_to_local(dt):
    """Convert time to local time format"""
    if not timezone.is_aware(dt):
        dt = timezone.make_aware(dt)
    local_time = timezone.localtime(dt)
    return local_time.strftime("%H:%M")

def extract_number(text):
    """استخراج اعداد از متن با پشتیبانی از تمام فرمت‌ها"""
    if not text:
        return 0
    
    # حذف تمام کاراکترهای غیرعددی (به جز نقطه و ویرگول)
    cleaned = re.sub(r'[^\d٫,]', '', text)
    
    # جایگزینی جداکننده‌های فارسی و انگلیسی
    cleaned = cleaned.replace('٫', '').replace(',', '')
    
    # استخراج تمام ارقام
    numbers = re.findall(r'\d+', cleaned)
    
    return int(''.join(numbers)) if numbers else 0
# -------------------- Base Scraper Class --------------------

class BaseScraper:
    """Base class for travel information scrapers"""
    
    def __init__(self):
        self.driver = None
        
    def setup_driver(self):
        """Setup selenium driver"""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('--disable-web-security')
        options.add_argument('--disable-extensions')
        
        # Disable SSL verification
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ssl-protocol=any')
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements
        
    def extract_trip_data(self, element, date):
        try:
            origin = element.find_element(By.CLASS_NAME, 'location').text.strip()
            destination = element.find_elements(By.CLASS_NAME, 'location')[1].text.strip()
            time = element.find_element(By.CLASS_NAME, 'time-container').text.strip()
            price = extract_number(element.find_element(By.CLASS_NAME, 'payable-price').text)
            capacity = extract_number(element.find_element(By.CLASS_NAME, 'capacity-text').text)
            type_class = element.find_element(By.CLASS_NAME, 'title').text.strip()
            
            return {
                'origin': origin,
                'destination': destination,
                'time': time,
                'price': price,
                'capacity': capacity,
                'type_class': type_class,
                'date': date
            }
        except Exception as e:
            logger.error(f"Error extracting trip data: {e}")
            return None
    def _create_trip_object(self, model_class, trip_data):
        """Create model object from extracted data"""
        if not trip_data:
            return None
            
        try:
            departure_datetime = timezone.make_aware(datetime.strptime(
                f"{trip_data['date']} {trip_data['time']}", "%Y-%m-%d %H:%M"
            ))
            
            # Get weather for destination city
            weather = get_weather(trip_data['destination'])
            
            # Get calendar events for departure date
            calendar_event = get_calendar_events(departure_datetime.date())
            
            # Create the trip object
            trip = model_class.objects.create(
                origin=trip_data['origin'],
                destination=trip_data['destination'],
                departure_datetime=departure_datetime,
                price=trip_data['price'],
                capacity=trip_data['capacity'],
                type_of_class=trip_data['type_class'],
                calendar_event=calendar_event,
                weather=weather  # Add weather directly if available
            )
            
            return trip
            
        except Exception as e:
            logger.error(f"Error creating trip object: {str(e)}")
            return None
# -------------------- Flight Scraper --------------------

class FlightScraper(BaseScraper):
    """Scraper for flights"""
    
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.mrbilit.com/flights"

    def get_flights(self, date, origin, destination):
        """Get flights information"""
        try:
            self.setup_driver()
            url = f"{self.base_url}/{origin}-{destination}?departureDate={date}"
            logger.info(f"Fetching flights from: {url}")
            
            self.driver.get(url)
            time.sleep(5)  # Wait for page to load
            
            flights = []
            flight_elements = self.driver.find_elements(By.CLASS_NAME, 'trip-card-container')
            logger.info(f"Found {len(flight_elements)} flights")
            
            for element in flight_elements:
                flight_data = self.extract_trip_data(element, date)
                if flight_data:
                    flight_obj = self._create_trip_object(Flight, flight_data)
                    if flight_obj:
                        flights.append(flight_obj)
            
            return flights
        except Exception as e:
            logger.error(f"Error getting flights: {str(e)}")
            return []
        finally:
            if self.driver:
                self.driver.quit()

# -------------------- Bus Scraper --------------------

class BusScraper(BaseScraper):
    """Scraper for buses"""
    
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.mrbilit.com/buses"

    def get_buses(self, date, origin, destination):
        """Get buses information"""
        try:
            self.setup_driver()
            url = f"{self.base_url}/{origin}-{destination}?departureDate={date}"
            logger.info(f"Fetching buses from: {url}")
            
            self.driver.get(url)
            time.sleep(5)
            
            buses = []
            bus_elements = self.driver.find_elements(By.CLASS_NAME, 'trip-card-container')
            logger.info(f"Found {len(bus_elements)} buses")
            
            for element in bus_elements:
                bus_data = self.extract_trip_data(element, date)
                if bus_data:
                    bus_obj = self._create_trip_object(Bus, bus_data)
                    if bus_obj:
                        buses.append(bus_obj)
            
            return buses
        except Exception as e:
            logger.error(f"Error getting buses: {str(e)}")
            return []
        finally:
            if self.driver:
                self.driver.quit()

# -------------------- Train Scraper --------------------

class TrainScraper(BaseScraper):
    """Scraper for trains"""
    
    def __init__(self):
        super().__init__()
        self.base_url = "https://www.mrbilit.com/trains"

    def get_trains(self, date, origin, destination):
        """Get trains information"""
        try:
            self.setup_driver()
            url = f"{self.base_url}/{origin}-{destination}?departureDate={date}"
            logger.info(f"Fetching trains from: {url}")
            
            self.driver.get(url)
            time.sleep(5)
            
            trains = []
            train_elements = self.driver.find_elements(By.CLASS_NAME, 'trip-card-container')
            logger.info(f"Found {len(train_elements)} trains")
            
            for element in train_elements:
                train_data = self.extract_trip_data(element, date)
                if train_data:
                    train_obj = self._create_trip_object(Train, train_data)
                    if train_obj:
                        trains.append(train_obj)
            
            return trains
        except Exception as e:
            logger.error(f"Error getting trains: {str(e)}")
            return []
        finally:
            if self.driver:
                self.driver.quit()

# -------------------- API Functions --------------------

def get_weather(city_name):
    """Get weather information from OpenWeatherMap API"""
    try:
        if not city_name:
            logger.warning("City name is empty")
            return None

        # First try to get existing weather data that's not too old (e.g. less than 1 hour old)
        one_hour_ago = timezone.now() - timezone.timedelta(hours=1)
        existing_weather = Weather.objects.filter(
            city=city_name,
            request_date_time__gte=one_hour_ago
        ).first()

        if existing_weather:
            return existing_weather

        params = {
            "q": city_name,
            "appid": settings.OPENWEATHERMAP_API_KEY,
            "units": "metric",
            "lang": "fa"
        }

        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=params,
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        weather_data = {
            'city': city_name,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'temp_min': data['main'].get('temp_min'),
            'temp_max': data['main'].get('temp_max'),
            'humidity': data['main'].get('humidity'),
            'pressure': data['main'].get('pressure'),
            'wind_speed': data.get('wind', {}).get('speed', 0),
            'icon': data['weather'][0].get('icon', '01d')
        }

        weather, created = Weather.objects.update_or_create(
            city=city_name,
            defaults=weather_data
        )

        return weather

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error getting weather for {city_name}: {str(e)}")
    except KeyError as e:
        logger.error(f"Key error in weather data for {city_name}: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error getting weather for {city_name}: {str(e)}")

    return None

def clean_event_text(event_text):
    """Remove Gregorian dates in brackets from event text"""
    if not event_text:
        return event_text
    
    # Remove all occurrences of [DD Month] or similar patterns
    cleaned_text = re.sub(r'\s*\[.*?\]\s*', '', event_text)
    # Remove any extra commas left after cleaning
    cleaned_text = re.sub(r',\s*,', ',', cleaned_text).strip(', ')
    return cleaned_text

def get_calendar_events(date):
    """Get calendar events from API"""
    try:
        params = {
            'year': date.year,
            'month': date.month,
            'day': date.day
        }
        
        response = requests.get(
            "https://pnldev.com/api/calender",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        
        data = response.json()
        logger.info("Calendar data received")
        
        if data.get('status'):
            result = data['result']
            raw_events = ", ".join(result.get('event', [])) or None
            
            # Clean events text by removing Gregorian dates
            cleaned_events = clean_event_text(raw_events) if raw_events else None

            event, created = CalendarEvent.objects.update_or_create(
                date=date,
                defaults={
                    'is_holiday': result.get('holiday', False),
                    'solar_year': result['solar']['year'],
                    'solar_month': result['solar']['month'],
                    'solar_day': result['solar']['day'],
                    'events': cleaned_events  # Use cleaned version
                }
            )
            
            return event
        return None
    except Exception as e:
        logger.error(f"Error getting calendar events: {str(e)}")
        return None

# -------------------- Public Interface --------------------

def get_flights(date, origin, destination):
    """Public interface for getting flights"""
    return FlightScraper().get_flights(date, origin, destination)

def get_buses(date, origin, destination):
    """Public interface for getting buses"""
    return BusScraper().get_buses(date, origin, destination)

def get_trains(date, origin, destination):
    """Public interface for getting trains"""
    return TrainScraper().get_trains(date, origin, destination)

