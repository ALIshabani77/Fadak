# import schedule
# import time
# from .crawler import MrBilitCrawler
# from .config import SCHEDULE

# def run_crawler():
#     print("Starting crawler...")
#     crawler = MrBilitCrawler()
#     crawler.crawl()
#     print("Crawling completed!")

# def start_scheduler():
#     # اجرای اولیه
#     run_crawler()
    
#     # زمان‌بندی دوره‌ای
#     schedule.every(SCHEDULE["interval_minutes"]).minutes.do(run_crawler)
    
#     while True:
#         schedule.run_pending()
#         time.sleep(60)




# import schedule
# import time
# from .crawler import MrBilitCrawler
# from .config import SCHEDULE

# def run_crawler():
#     print("🔄 در حال دریافت اطلاعات جدید...")
#     crawler = MrBilitCrawler()
#     crawler.crawl()
#     print("✅ اطلاعات با موفقیت ذخیره شد")

# def start_scheduler():
#     # اجرای اولیه
#     run_crawler()
    
#     # زمان‌بندی هر 1 دقیقه
#     schedule.every(SCHEDULE["interval_minutes"]).minutes.do(run_crawler)
    
#     print(f"⏰ کراولر هر {SCHEDULE['interval_minutes']} دقیقه اجرا خواهد شد")
    
#     while True:
#         schedule.run_pending()
#         time.sleep(1)  # چک هر 1 ثانیه

# if __name__ == "__main__":
#     start_scheduler()






import schedule
import time
from .crawler import MrBilitCrawler
from .config import SCHEDULE
from ..models import CrawlerStatus

def run_crawler():
    print("🔄 در حال دریافت اطلاعات جدید...")
    try:
        crawler = MrBilitCrawler()
        crawler.crawl()
        print("✅ اطلاعات با موفقیت ذخیره شد")
    except Exception as e:
        print(f"❌ خطا در اجرای کراولر: {e}")

def start_scheduler():
    # اجرای اولیه
    run_crawler()
    
    # زمان‌بندی هر 1 دقیقه
    schedule.every(SCHEDULE["interval_minutes"]).minutes.do(run_crawler)
    
    print(f"⏰ کراولر هر {SCHEDULE['interval_minutes']} دقیقه اجرا خواهد شد")
    
    while True:
        schedule.run_pending()
        time.sleep(1)  # چک هر 1 ثانیه

if __name__ == "__main__":
    start_scheduler()