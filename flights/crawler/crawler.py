from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .config import MRBILIT, BROWSER,SCHEDULE
from .database import Database
import time
from datetime import datetime, timedelta
from flights.models import CrawlerStatus

class MrBilitCrawler:
    def __init__(self):
        self.db = Database()
        self.driver = self._init_driver()
        self.crawler_status = {
            'flight': {'items': 0, 'error': None},
            'train': {'items': 0, 'error': None},
            'bus': {'items': 0, 'error': None}
        }
    
    def _init_driver(self):
        options = webdriver.ChromeOptions()
        if BROWSER["headless"]:
            options.add_argument('--headless')
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.set_page_load_timeout(BROWSER["timeout"])
        return driver
    
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
        try:
            for ticket_type in ["flight", "train", "bus"]:
                self._crawl_ticket_type(ticket_type)
            
            # Save final status
            for crawler_type, status in self.crawler_status.items():
                self._save_crawler_status(
                    crawler_type,
                    status['items'],
                    status['error']
                )
                
        except Exception as e:
            print(f"Error in main crawl: {e}")
        finally:
            self.driver.quit()
            self.db.close()
    
    def _crawl_ticket_type(self, ticket_type):
        base_url = f"{MRBILIT['base_url']}{MRBILIT['endpoints'][ticket_type]}"
        
        for date in self._get_future_dates():
            url = f"{base_url}?date={date}"
            self.driver.get(url)
            
            try:
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
                        print(f"Error processing item: {e}")
                        continue
                
                if tickets:
                    self.db.save_tickets(tickets)
                    self.crawler_status[ticket_type]['items'] += len(tickets)
                
                time.sleep(2)  # تاخیر بین درخواست‌ها
            
            except Exception as e:
                error_msg = f"Error crawling {ticket_type} for date {date}: {e}"
                print(error_msg)
                self.crawler_status[ticket_type]['error'] = error_msg



