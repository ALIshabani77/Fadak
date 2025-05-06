# تنظیمات اصلی کراولر
MRBILIT = {
    "base_url": "https://www.mrbilit.com",
    "endpoints": {
        "flight": "/flight",
        "train": "/train",
        "bus": "/bus"
    },
    "selectors": {
        "list_container": ".ticket-list",
        "item": ".ticket-item",
        "carrier": ".carrier-name",
        "departure": ".departure-city",
        "arrival": ".arrival-city",
        "price": ".price-amount",
        "departure_time": ".departure-time",
        "arrival_time": ".arrival-time",
        "date": ".departure-date"
    },
    "search_days": 10  # تعداد روزهای آینده برای جستجو
}

DATABASE = {
    "db_name": "flights_data.db",
    "table_name": "tickets"
}

SCHEDULE = {
    "interval_minutes": 1,
    "retry_attempts": 3
}

BROWSER = {
    "headless": True,
    "timeout": 30
}