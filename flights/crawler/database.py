import sqlite3
from datetime import datetime
from ..crawler.config import DATABASE

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE["db_name"])
        self._create_table()
    
    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {DATABASE["table_name"]} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            carrier TEXT,
            departure TEXT,
            arrival TEXT,
            departure_date TEXT,
            departure_time TEXT,
            arrival_time TEXT,
            price REAL,
            crawl_time TEXT
        )
        """)
        self.conn.commit()
    
    def save_tickets(self, tickets):
        cursor = self.conn.cursor()
        try:
            for ticket in tickets:
                cursor.execute(f"""
                INSERT INTO {DATABASE["table_name"]} VALUES (
                    NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?
                )
                """, (
                    ticket['type'],
                    ticket['carrier'],
                    ticket['departure'],
                    ticket['arrival'],
                    ticket['date'],
                    ticket['departure_time'],
                    ticket['arrival_time'],
                    ticket['price'],
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ))
            self.conn.commit()
        except Exception as e:
            print(f"Error saving tickets: {e}")
    
    def close(self):
        self.conn.close()