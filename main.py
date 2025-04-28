import os
import sys
import django
import time
import logging
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

# 1. تنظیم محیط Django قبل از ایمپورت مدل‌ها
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sellei.settings')
django.setup()

# 2. ایمپورت مدل‌های Django بعد از تنظیم محیط
from django.utils import timezone
from flights.models import Flight, Bus, Train, Weather, CalendarEvent, CrawlerStatus

# 3. تنظیمات لاگینگ
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('crawler.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

def setup_driver():
    """تنظیم و راه‌اندازی درایور Chrome"""
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        driver.implicitly_wait(10)
        return driver
    except Exception as e:
        logging.error(f"خطا در راه‌اندازی درایور: {str(e)}")
        raise

def create_weather(city):
    """ایجاد رکورد آب و هوا"""
    try:
        weather = Weather.objects.create(
            city=city,
            temperature=25.5,
            temp_min=22.0,
            temp_max=28.0,
            humidity=65,
            pressure=1012,
            wind_speed=12,
            weather_description="آفتابی"
        )
        return weather
    except Exception as e:
        logging.error(f"خطا در ایجاد رکورد آب و هوا: {str(e)}")
        return None

def create_calendar_event(date):
    """ایجاد رکورد رویداد تقویمی"""
    try:
        event = CalendarEvent.objects.create(
            date=date,
            is_holiday=False,
            solar_year=date.year,
            solar_month=date.month,
            solar_day=date.day,
            events={"مناسبت": "بدون مناسبت خاص"}
        )
        return event
    except Exception as e:
        logging.error(f"خطا در ایجاد رکورد تقویم: {str(e)}")
        return None

def crawl_flights(driver, date):
    """کراولینگ و ذخیره اطلاعات پروازها"""
    try:
        # نمونه داده‌های پرواز (جایگزین با داده‌های واقعی کراول شده)
        weather = create_weather("تهران")
        calendar_event = create_calendar_event(date)
        
        flight = Flight.objects.create(
            origin="تهران",
            destination="مشهد",
            price=500000,
            capacity=150,
            type_of_class="اقتصادی",
            departure_datetime=date,
            flight_number="IR123",
            airline="ایران ایر",
            duration=timedelta(hours=1, minutes=30),
            weather=weather,
            calendar_event=calendar_event
        )
        
        CrawlerStatus.objects.create(
            crawler_type='flight',
            last_run=timezone.now(),
            next_run=timezone.now() + timedelta(minutes=1),
            status='completed',
            items_crawled=1,
            flight_data=flight
        )
        
        logging.info(f"اطلاعات پرواز برای تاریخ {date} با موفقیت ذخیره شد")
        return True
    except Exception as e:
        CrawlerStatus.objects.create(
            crawler_type='flight',
            last_run=timezone.now(),
            next_run=timezone.now() + timedelta(minutes=1),
            status='failed',
            error_message=str(e)
        )
        logging.error(f"خطا در ذخیره اطلاعات پرواز: {str(e)}")
        return False

def crawl_buses(driver, date):
    """کراولینگ و ذخیره اطلاعات اتوبوس‌ها"""
    try:
        weather = create_weather("تهران")
        calendar_event = create_calendar_event(date)
        
        bus = Bus.objects.create(
            origin="تهران",
            destination="مشهد",
            price=250000,
            capacity=40,
            type_of_class="VIP",
            departure_datetime=date,
            bus_company="تسپا",
            bus_type="ویژه",
            amenities=["TV", "WiFi"],
            weather=weather,
            calendar_event=calendar_event
        )
        
        CrawlerStatus.objects.create(
            crawler_type='bus',
            last_run=timezone.now(),
            next_run=timezone.now() + timedelta(minutes=1),
            status='completed',
            items_crawled=1,
            bus_data=bus
        )
        
        logging.info(f"اطلاعات اتوبوس برای تاریخ {date} با موفقیت ذخیره شد")
        return True
    except Exception as e:
        CrawlerStatus.objects.create(
            crawler_type='bus',
            last_run=timezone.now(),
            next_run=timezone.now() + timedelta(minutes=1),
            status='failed',
            error_message=str(e)
        )
        logging.error(f"خطا در ذخیره اطلاعات اتوبوس: {str(e)}")
        return False

def crawl_trains(driver, date):
    """کراولینگ و ذخیره اطلاعات قطارها"""
    try:
        weather = create_weather("تهران")
        calendar_event = create_calendar_event(date)
        
        train = Train.objects.create(
            origin="تهران",
            destination="مشهد",
            price=350000,
            capacity=300,
            type_of_class="کوپه‌ای",
            departure_datetime=date,
            train_number="123",
            train_type="مسافری",
            wagon_count=10,
            weather=weather,
            calendar_event=calendar_event
        )
        
        CrawlerStatus.objects.create(
            crawler_type='train',
            last_run=timezone.now(),
            next_run=timezone.now() + timedelta(minutes=1),
            status='completed',
            items_crawled=1,
            train_data=train
        )
        
        logging.info(f"اطلاعات قطار برای تاریخ {date} با موفقیت ذخیره شد")
        return True
    except Exception as e:
        CrawlerStatus.objects.create(
            crawler_type='train',
            last_run=timezone.now(),
            next_run=timezone.now() + timedelta(minutes=1),
            status='failed',
            error_message=str(e)
        )
        logging.error(f"خطا در ذخیره اطلاعات قطار: {str(e)}")
        return False

def main_crawl():
    """تابع اصلی اجرای کراولر"""
    driver = None
    try:
        driver = setup_driver()
        logging.info("🔄 در حال دریافت اطلاعات جدید...")
        
        today = datetime.now().date()
        for i in range(10):  # برای 10 روز آینده
            current_date = today + timedelta(days=i)
            
            if not crawl_flights(driver, current_date):
                driver.quit()
                driver = setup_driver()
                
            if not crawl_trains(driver, current_date):
                driver.quit()
                driver = setup_driver()
                
            if not crawl_buses(driver, current_date):
                driver.quit()
                driver = setup_driver()
                
        logging.info("✅ اطلاعات با موفقیت ذخیره شد")
    except Exception as e:
        logging.error(f"خطای اصلی در کراولینگ: {str(e)}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    while True:
        start_time = time.time()
        main_crawl()
        
        # محاسبه زمان باقیمانده تا اجرای بعدی
        elapsed_time = time.time() - start_time
        wait_time = max(60 - elapsed_time, 0)
        
        logging.info(f"⏳ اجرای بعدی در {wait_time:.1f} ثانیه دیگر...")
        time.sleep(wait_time)
        logging.info("🔄 شروع مجدد کراولر...")