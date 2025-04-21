# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sellei.settings')
# django.setup()

from unittest.mock import patch, MagicMock
from django.test import TestCase
from datetime import datetime
from django.utils import timezone
from flights.utils import (
    gregorian_to_jalali,
    convert_time_to_local,
    extract_number,
    get_weather,
    get_calendar_events,
    get_flights,
    get_buses,
    get_trains,
    BaseScraper
)
from flights.models import Weather, CalendarEvent, Flight, Bus, Train
from selenium.webdriver.common.by import By

class UtilsFunctionTests(TestCase):
    """Test utility functions"""
    
    def test_gregorian_to_jalali(self):
        test_date = timezone.make_aware(datetime(2023, 10, 15, 12, 30))
        result = gregorian_to_jalali(test_date)
        self.assertEqual(result, "1402-07-23 12:30")

    def test_convert_time_to_local(self):
        test_time = timezone.make_aware(datetime(2023, 10, 15, 12, 30))
        result = convert_time_to_local(test_time)
        self.assertEqual(result, "12:30")

    def test_extract_number(self):
        self.assertEqual(extract_number("قیمت: ۱,۲۰۰,۰۰۰ تومان"), 1200000)
        self.assertEqual(extract_number("1,200,000"), 1200000)
        self.assertEqual(extract_number("1200000"), 1200000)
        self.assertEqual(extract_number("ظرفیت: 42 صندلی"), 42)
        self.assertEqual(extract_number("بدون عدد"), 0)

class APIFunctionsTests(TestCase):
    """Test API functions"""
    
    @patch('requests.get')
    def test_get_weather(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "weather": [{"description": "آسمان صاف", "icon": "01d"}],
            "main": {"temp": 25.5, "humidity": 40},
            "wind": {"speed": 5.5},
            "name": "تهران"
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        weather = get_weather("تهران")
        self.assertIsNotNone(weather)
        self.assertEqual(weather.city, "تهران")
        self.assertEqual(weather.temperature, 25.5)
        self.assertEqual(weather.icon, "01d")

    @patch('requests.get')
    def test_get_calendar_events(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "status": True,
            "result": {
                "solar": {"year": 1402, "month": 7, "day": 23},
                "event": ["روز جهانی عصای سفید"],
                "holiday": False
            }
        }
        mock_get.return_value = mock_response
        
        date = datetime(2023, 10, 15).date()
        event = get_calendar_events(date)
        self.assertEqual(event.solar_year, 1402)
        self.assertIn("عصای سفید", event.events)

class ScraperTests(TestCase):
    """Test scraper classes"""
    
    def setUp(self):
        self.test_date = "2023-10-15"
        self.origin = "THR"
        self.destination = "MHD"
        
        # Create mock element with proper structure
        self.mock_element = MagicMock()
        
        # Setup mock elements for find_element
        self.origin_mock = MagicMock()
        self.origin_mock.text = "مبدا"
        
        self.destination_mock = MagicMock()
        self.destination_mock.text = "مقصد"
        
        self.time_mock = MagicMock()
        self.time_mock.text = "12:30"
        
        self.price_mock = MagicMock()
        self.price_mock.text = "1,200,000 تومان"
        
        self.capacity_mock = MagicMock()
        self.capacity_mock.text = "42 صندلی"
        
        self.class_mock = MagicMock()
        self.class_mock.text = "اکونومی"

        # Setup find_elements for locations
        self.mock_element.find_elements.return_value = [
            self.origin_mock,
            self.destination_mock
        ]

    @patch('selenium.webdriver.Chrome')
    @patch('webdriver_manager.chrome.ChromeDriverManager.install')
    def test_base_scraper(self, mock_install, mock_chrome):
        scraper = BaseScraper()
        scraper.driver = MagicMock()
        
        # Setup find_element side_effect in correct order
        self.mock_element.find_element.side_effect = [
            self.origin_mock,        # find_element(By.CLASS_NAME, 'location')
            self.time_mock,          # find_element(By.CLASS_NAME, 'time-container')
            self.price_mock,         # find_element(By.CLASS_NAME, 'payable-price')
            self.capacity_mock,      # find_element(By.CLASS_NAME, 'capacity-text')
            self.class_mock           # find_element(By.CLASS_NAME, 'title')
        ]
        
        # Execute
        trip_data = scraper.extract_trip_data(self.mock_element, self.test_date)
        
        # Verify
        self.assertEqual(trip_data['origin'], "مبدا") # Ensure origin is extracted correctly
        self.assertEqual(trip_data['destination'], "مقصد") # Removed this assertion
        self.assertEqual(trip_data['time'], "12:30")
        self.assertEqual(trip_data['price'], 1200000)
        self.assertEqual(trip_data['capacity'], 42)
        self.assertEqual(trip_data['type_class'], "اکونومی")

    @patch('flights.utils.FlightScraper.get_flights')
    def test_flight_scraper(self, mock_get_flights):
        mock_get_flights.return_value = [MagicMock(origin='THR', destination='MHD', price=1200000)]
        flights = get_flights(self.test_date, self.origin, self.destination)
        self.assertEqual(len(flights), 1)
        self.assertEqual(flights[0].origin, 'THR')

    @patch('flights.utils.BusScraper.get_buses')
    def test_bus_scraper(self, mock_get_buses):
        mock_get_buses.return_value = [MagicMock(origin='تهران', destination='مشهد', price=500000)]
        buses = get_buses(self.test_date, self.origin, self.destination)
        self.assertEqual(len(buses), 1)
        self.assertEqual(buses[0].origin, 'تهران')

    @patch('flights.utils.TrainScraper.get_trains')
    def test_train_scraper(self, mock_get_trains):
        mock_get_trains.return_value = [MagicMock(origin='تهران', destination='مشهد', price=800000)]
        trains = get_trains(self.test_date, self.origin, self.destination)
        self.assertEqual(len(trains), 1)
        self.assertEqual(trains[0].origin, 'تهران')
