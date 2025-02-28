from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json 

def get_flights(date, origin, destination):
         
         chrome_options = Options()
         chrome_options.add_argument("--headless")  
         chrome_options.add_argument("--disable-gpu")  
         chrome_options.add_argument("--no-sandbox")  

         
         service = Service('C:\\Users\\fx506heb\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  # مسیر chromedriver رو تنظیم کن

         
         driver = webdriver.Chrome(service=service, options=chrome_options)

         try:
             
             url = f"https://www.mrbilit.com/flights/{origin}-{destination}?adultCount=1&departureDate={date}"
             driver.get(url)

             
             time.sleep(10)

             
             flights = []  
             flight_elements = driver.find_elements(By.CLASS_NAME, 'trip-card-container')  
             for flight in flight_elements:
                 origin = flight.find_elements(By.CLASS_NAME, 'location')[0].text.strip()
                 print(origin)
                 destination = flight.find_elements(By.CLASS_NAME, 'location')[1].text.strip()
                 print(destination)
                 time_str = flight.find_elements(By.CLASS_NAME, 'time-container')[0].text.strip()
                 print(time_str)
                 price = flight.find_elements(By.CLASS_NAME, 'payable-price')[0].text.strip()
                 capacity = flight.find_elements(By.CLASS_NAME, 'capacity-text')[0].text.strip()
                 print(capacity)
                 type_of_clases = flight.find_elements(By.CLASS_NAME, 'title')[0].text.strip()
                 print(type_of_clases)
                 print('-----------------------')

                 flight_data = {
                     "origin": origin,
                     "destination": destination,
                     "time": time_str,
                     "price": price,
                     "capacity": capacity,
                     "type_of_clases": type_of_clases,
                 }

                 flights.append(flight_data)

                 flights_json = json.dumps(flights, ensure_ascii=False, indent=4)  

                 with open('flights.json', 'w', encoding='utf-8') as f:
                    f.write(flights_json)

                 return flights_json
             
         finally:
             
             driver.quit()



















