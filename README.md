<div align="center">

# ✈️ سامانه فروش و agregator بلیط سفر (پروژه فدک)

<a href="https://github.com/ALIshabani77/Fadak">
  <img src="screenshot.png" alt="نمایی از پروژه" width="800"/>
</a>

<br>

<p>
  یک سیستم هوشمند برای جمع‌آوری و ارائه اطلاعات بلیط‌های سفر با استفاده از Web Scraping و Django REST Framework.
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/DRF-3.x-red?style=for-the-badge&logo=django-rest-framework" alt="DRF">
  <img src="https://img.shields.io/badge/Selenium-4.x-yellow?style=for-the-badge&logo=selenium" alt="Selenium">
</p>

</div>

---

<details>
  <summary>📜 **فهرست مطالب**</summary>
  <ol>
    <li><a href="#-درباره-پروژه">درباره پروژه</a></li>
    <li><a href="#-ویژگی‌های-کلیدی">ویژگی‌های کلیدی</a></li>
    <li><a href="#-تکنولوژی‌های-استفاده-شده">تکنولوژی‌های استفاده شده</a></li>
    <li><a href="#-ساختار-پروژه">ساختار پروژه</a></li>
    <li><a href="#-نصب-و-راه‌اندازی">نصب و راه‌اندازی</a></li>
    <li><a href="#-مشارکت-در-پروژه">مشارکت در پروژه</a></li>
    <li><a href="#-لایسنس">لایسنس</a></li>
  </ol>
</details>

---

## 🚀 درباره پروژه

> **پروژه فدک** یک سیستم هوشمند برای جمع‌آوری و ارائه اطلاعات بلیط‌های سفر (شامل **پرواز، قطار و اتوبوس**) است. این سامانه با استفاده از تکنیک‌های Web Scraping به صورت خودکار اطلاعات را از سایت‌های مرجع فروش بلیط استخراج کرده و آن‌ها را از طریق یک API قدرتمند در اختیار کاربران قرار می‌دهد. هدف اصلی این پروژه، ایجاد یک پلتفرم جامع برای دسترسی سریع و آسان به آخرین وضعیت بلیط‌ها و رویدادهای تقویمی است.

## ✨ ویژگی‌های کلیدی

* 🤖 **جمع‌آوری خودکار داده (Crawling):** استخراج اطلاعات دقیق بلیط (مبدأ، مقصد، قیمت، ظرفیت) با استفاده از `Selenium`.
* 🗃️ **پایگاه داده قدرتمند:** طراحی مدل‌های داده‌ای بهینه با Django ORM برای ذخیره‌سازی اطلاعات سفر و رویدادهای تقویمی.
* 🔌 **API جامع:** ارائه اطلاعات بلیط‌ها و وضعیت آب و هوا از طریق یک API امن و سریع که با `Django REST Framework` توسعه داده شده است.
* ⚙️ **پنل مدیریت پیشرفته:** پنل ادمین سفارشی‌سازی شده برای مدیریت کامل بلیط‌ها، مشاهده گزارش‌های کراولر و مدیریت رویدادها.
* 🕒 **زمان‌بندی هوشمند:** اجرای خودکار اسکریپت‌های کراولر در بازه‌های زمانی مشخص برای به‌روز نگه داشتن اطلاعات.

## 🛠️ تکنولوژی‌های استفاده شده

| دسته          | تکنولوژی‌ها                                       |
| :------------ | :------------------------------------------------- |
| **Backend** | `Python`, `Django`                                 |
| **API** | `Django REST Framework`                            |
| **Web Scraping**| `Selenium`, `ChromeDriver`                         |
| **Database** | `SQLite` (پیش‌فرض), `PostgreSQL` (پیشنهادی)        |
| **Deployment** | `Docker`, `Liara`                                  |

## 📂 ساختار پروژه

<details>
  <summary>برای مشاهده ساختار پروژه کلیک کنید</summary>

```sh
├── flights/                     # اپلیکیشن اصلی جنگو
│   ├── crawler/                 # ماژول‌های مربوط به Web Scraping
│   │   ├── crawler.py           # هسته اصلی کراولر
│   │   └── ...
│   ├── migrations/              # فایل‌های مایگریشن دیتابیس
│   ├── admin.py                 # تنظیمات پنل ادمین
│   ├── models.py                # مدل‌های پایگاه داده (ORM)
│   ├── serializers.py           # سریالایزرهای DRF
│   ├── urls.py                  # مسیرهای URL اپلیکیشن
│   └── views.py                 # ویوهای مربوط به API
├── sellei/                      # پوشه تنظیمات اصلی پروژه
│   ├── settings.py              # تنظیمات اصلی جنگو
│   └── urls.py                  # مسیرهای URL اصلی پروژه
├── manage.py                    # اسکریپت مدیریت جنگو
├── requirements.txt             # لیست وابستگی‌های پایتون
└── db.sqlite3                   # فایل پایگاه داده
```

</details>

## ⚙️ نصب و راه‌اندازی

برای اجرای این پروژه به صورت محلی، مراحل زیر را دنبال کنید:

1.  **کلون کردن ریپازیتوری:**
    ```bash
    git clone [https://github.com/ALIshabani77/Fadak.git](https://github.com/ALIshabani77/Fadak.git)
    cd Fadak
    ```

2.  **ساخت و فعال‌سازی محیط مجازی:**
    ```bash
    # for Windows
    python -m venv venv && venv\Scripts\activate

    # for macOS/Linux
    python3 -m venv venv && source venv/bin/activate
    ```

3.  **نصب وابستگی‌ها:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **اجرای مایگریشن‌ها:**
    ```bash
    python manage.py migrate
    ```

5.  **ساخت Superuser (برای دسترسی به پنل ادمین):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **اجرای سرور توسعه:**
    ```bash
    python manage.py runserver
    ```
    > پروژه در آدرس `http://127.0.0.1:8000` در دسترس خواهد بود.

## 🤝 مشارکت در پروژه

از مشارکت شما در این پروژه استقبال می‌کنیم! برای کمک به توسعه، لطفاً یک **Pull Request** ارسال کنید.

1.  پروژه را **Fork** کنید.
2.  یک **Branch** جدید بسازید (`git checkout -b feature/NewFeature`).
3.  تغییرات خود را **Commit** کنید (`git commit -m 'Add a new feature'`).
4.  تغییرات را به **Branch** خود **Push** کنید (`git push origin feature/NewFeature`).
5.  یک **Pull Request** باز کنید.

## 📝 لایسنس

این پروژه تحت لایسنس [MIT](https://choosealicense.com/licenses/mit/) منتشر شده است.

---

<p align="center">
  ساخته شده با ❤️ توسط <strong>علی شعبانی</strong>
</p>
<p align="center">
  <a href="https://github.com/ALIshabani77">GitHub</a>
</p>
