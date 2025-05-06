from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .config import MRBILIT, BROWSER, SCHEDULE
from .database import Database
import time
from datetime import datetime, timedelta
from flights.models import CrawlerStatus
import logging

logger = logging.getLogger(__name__)

class MrBilitCrawler:
    def __init__(self):
        self.db = Database()
        self.driver = None
        self.crawler_status = {
            'flight': {'items': 0, 'error': None},
            'train': {'items': 0, 'error': None},
            'bus': {'items': 0, 'error': None}
        }
        try:
            self.driver = self._init_driver()
        except Exception as e:
            logger.error(f"Failed to initialize WebDriver: {str(e)}")
            raise  # خطا را به سطح بالاتر منتقل می‌کنیم
    
    def _init_driver(self):
        """مقداردهی و پیکربندی WebDriver با مدیریت ایمن منابع"""
        driver = None
        try:
            options = webdriver.ChromeOptions()
            if BROWSER["headless"]:
                options.add_argument('--headless')
            
            # اضافه کردن برخی options برای پایداری بیشتر
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.set_page_load_timeout(BROWSER["timeout"])
            return driver
        except Exception as e:
            if driver is not None:
                driver.quit()  # در صورت خطا، درایور را می‌بندیم
            logger.error(f"WebDriver initialization failed: {str(e)}")
            raise  # خطا را به سطح بالاتر منتقل می‌کنیم
    
    def __enter__(self):
        """برای پشتیبانی از الگوی context manager"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """تضمین می‌کند منابع در هر حالتی آزاد شوند"""
        self.close_resources()
        if exc_type is not None:
            logger.error(f"Crawler exited with exception: {exc_val}")
    
    def close_resources(self):
        """بستن ایمن تمام منابع"""
        try:
            if self.driver is not None:
                self.driver.quit()
                self.driver = None
        except Exception as e:
            logger.error(f"Error closing WebDriver: {str(e)}")
        
        try:
            self.db.close()
        except Exception as e:
            logger.error(f"Error closing database connection: {str(e)}")
    
    def _get_future_dates(self):
        today = datetime.now()
        return [(today + timedelta(days=i)).strftime("%Y-%m-%d") 
                for i in range(1, MRBILIT["search_days"] + 1)]
    
    def _save_crawler_status(self, crawler_type, items, error=None):
        now = datetime.now()
        next_run = now + timedelta(minutes=SCHEDULE["interval_minutes"])
        
        CrawlerStatus.objects.create(
            crawler_type=crawler_type,
            last_run=now,
            next_run=next_run,
            status='success' if not error else 'failed',
            items_crawled=items,
            error_message=error,
            days_ahead=MRBILIT["search_days"]
        )
    
    def crawl(self):
        """متد اصلی برای اجرای کراولر با مدیریت خطا و منابع"""
        try:
            for ticket_type in ["flight", "train", "bus"]:
                self._crawl_ticket_type(ticket_type)
            
            # ذخیره وضعیت نهایی
            for crawler_type, status in self.crawler_status.items():
                self._save_crawler_status(
                    crawler_type,
                    status['items'],
                    status['error']
                )
                
        except Exception as e:
            logger.error(f"Error in main crawl: {str(e)}")
            # وضعیت خطا را برای تمام کراولرها ثبت می‌کنیم
            for crawler_type in self.crawler_status.keys():
                self._save_crawler_status(
                    crawler_type,
                    0,
                    f"General crawler error: {str(e)}"
                )
            raise  # خطا را به سطح بالاتر منتقل می‌کنیم
        finally:
            self.close_resources()
    
    def _crawl_ticket_type(self, ticket_type):
        """کراول کردن یک نوع بلیط خاص"""
        base_url = f"{MRBILIT['base_url']}{MRBILIT['endpoints'][ticket_type]}"
        
        for date in self._get_future_dates():
            url = f"{base_url}?date={date}"
            try:
                self.driver.get(url)
                
                WebDriverWait(self.driver, BROWSER["timeout"]).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, MRBILIT["selectors"]["list_container"])
                    )
                )
                
                items = self.driver.find_elements(
                    By.CSS_SELECTOR, MRBILIT["selectors"]["item"])
                
                tickets = []
                for item in items:
                    try:
                        ticket = {
                            "type": ticket_type,
                            "carrier": item.find_element(
                                By.CSS_SELECTOR, MRBILIT["selectors"]["carrier"]
                            ).text,
                            "departure": item.find_element(
                                By.CSS_SELECTOR, MRBILIT["selectors"]["departure"]
                            ).text,
                            "arrival": item.find_element(
                                By.CSS_SELECTOR, MRBILIT["selectors"]["arrival"]
                            ).text,
                            "price": float(item.find_element(
                                By.CSS_SELECTOR, MRBILIT["selectors"]["price"]
                            ).text.replace(",", "")),
                            "departure_time": item.find_element(
                                By.CSS_SELECTOR, MRBILIT["selectors"]["departure_time"]
                            ).text,
                            "arrival_time": item.find_element(
                                By.CSS_SELECTOR, MRBILIT["selectors"]["arrival_time"]
                            ).text,
                            "date": date
                        }
                        tickets.append(ticket)
                    except Exception as e:
                        logger.warning(f"Error processing {ticket_type} item: {str(e)}")
                        continue
                
                if tickets:
                    self.db.save_tickets(tickets)
                    self.crawler_status[ticket_type]['items'] += len(tickets)
                
                time.sleep(2)  # تاخیر بین درخواست‌ها
            
            except Exception as e:
                error_msg = f"Error crawling {ticket_type} for date {date}: {str(e)}"
                logger.error(error_msg)
                self.crawler_status[ticket_type]['error'] = error_msg
                # در صورت خطا به کراول کردن تاریخ‌های بعدی ادامه می‌دهیم