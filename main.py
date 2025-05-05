import os
import sys
import django
import time
import random
import logging
from datetime import datetime, timedelta
from django.utils import timezone
import jdatetime

# تنظیمات اولیه
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('master_bilet_crawler.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# تنظیم محیط Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sellei.settings')
django.setup()

from flights.models import Flight, Bus, Train, CrawlerStatus
from flights.utils import get_flights, get_buses, get_trains, get_weather, get_calendar_events

class MasterBiletCrawler:
    def __init__(self):
        self.max_retries = 3
        self.delay_between_attempts = 10
        self.delay_between_days = 15
        
        self.routes = {
            'flights': {'origin': 'THR', 'destination': 'MHD'},
            'buses': {'origin': 'tehran', 'destination': 'mashhad'},
            'trains': {'origin': 'tehran', 'destination': 'mashhad'}
        }

    def get_shamsi_date(self, date):
        jdate = jdatetime.date.fromgregorian(date=date)
        return f"{jdate.year}-{jdate.month:02d}-{jdate.day:02d}"

    def crawl_transport_data(self, date, transport_type):
        shamsi_date = self.get_shamsi_date(date)
        config = {
            'flights': {'name': 'پرواز', 'get_func': get_flights},
            'buses': {'name': 'اتوبوس', 'get_func': get_buses},
            'trains': {'name': 'قطار', 'get_func': get_trains}
        }[transport_type]
        
        route = self.routes[transport_type]
        
        for attempt in range(self.max_retries):
            try:
                logging.info(f"در حال دریافت {config['name']}ها از {route['origin']} به {route['destination']} برای تاریخ {shamsi_date}")
                results = config['get_func'](shamsi_date, route['origin'], route['destination'])
                
                if results:
                    logging.info(f"✅ {len(results)} {config['name']} دریافت شد")
                    return results
                else:
                    logging.warning(f"⚠️ هیچ {config['name']}ی یافت نشد")
                    return []
                    
            except Exception as e:
                if attempt == self.max_retries - 1:
                    logging.error(f"❌ خطا در دریافت {config['name']}ها: {str(e)}")
                else:
                    time.sleep(random.randint(self.delay_between_attempts, self.delay_between_attempts + 5))
        
        return []

    def crawl_for_date(self, date):
        shamsi_date = self.get_shamsi_date(date)
        result = {'flights': [], 'buses': [], 'trains': [], 'weather': None, 'calendar_event': None}
        
        try:
            logging.info(f"\n{'='*50}\n📅 شروع پردازش برای تاریخ: {shamsi_date}\n{'='*50}")
            
            # دریافت اطلاعات تقویم و آب و هوا
            result['calendar_event'] = get_calendar_events(date)
            result['weather'] = get_weather("مشهد")
            
            # کراول داده‌ها
            result['flights'] = self.crawl_transport_data(date, 'flights')
            result['buses'] = self.crawl_transport_data(date, 'buses')
            result['trains'] = self.crawl_transport_data(date, 'trains')
            
            # ذخیره وضعیت کراولر
            CrawlerStatus.objects.create(
                crawler_type='all',
                last_run=timezone.now(),
                next_run=timezone.now() + timedelta(hours=6),
                status='completed',
                items_crawled=len(result['flights']) + len(result['buses']) + len(result['trains'])
            )
            
            return result
            
        except Exception as e:
            logging.error(f"🚨 خطا در کراولینگ: {str(e)}")
            return None

def main():
    crawler = MasterBiletCrawler()
    
    try:
        days_to_crawl = 3
        start_date = datetime.now().date()
        
        for i in range(days_to_crawl):
            current_date = start_date + timedelta(days=i)
            result = crawler.crawl_for_date(current_date)
            
            if result:
                shamsi_date = crawler.get_shamsi_date(current_date)
                logging.info(f"\n{'='*50}\nنتایج برای تاریخ {shamsi_date}:")
                logging.info(f"- پروازها: {len(result['flights'])} مورد")
                logging.info(f"- اتوبوس‌ها: {len(result['buses'])} مورد")
                logging.info(f"- قطارها: {len(result['trains'])} مورد")
            
            if i < days_to_crawl - 1:
                time.sleep(crawler.delay_between_days)
                
    except KeyboardInterrupt:
        logging.info("\n🛑 دریافت سیگنال توقف")
    except Exception as e:
        logging.error(f"\n💣 خطای غیرمنتظره: {str(e)}")
    finally:
        logging.info("\n🏁 پایان عملیات کراولینگ")

if __name__ == "__main__":
    logging.info("\n🌟 شروع برنامه کراولر مستر بلیط")
    main()