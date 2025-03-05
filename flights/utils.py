from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import json 
import os

def get_flights(date, origin, destination):
         
         chrome_options = Options()
         chrome_options.add_argument("--headless")  
         chrome_options.add_argument("--disable-gpu")  
         chrome_options.add_argument("--no-sandbox")  

         
        #  chromedriver_path = os.path.expanduser('C:\Users\fx506heb\Downloads\chromedriver-linux64\chromedriver-linux64')  # مسیر chromedriver در پوشه خانگی
         chromedriver_path = 'chromedriver'
         service = Service(chromedriver_path)

         
        #  service = Service('C:\\Users\\fx506heb\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  

         
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
                 #return flights

                 flights_json = json.dumps(flights, ensure_ascii=False, indent=4)  

                 with open('flights.json', 'w', encoding='utf-8') as f:
                    f.write(flights_json)

                 return flights_json
             
         finally:
             
             driver.quit()



def get_bus(date, origin, destination):

        chrome_options= Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        chromedriver_path = 'chromedriver'
        service = Service(chromedriver_path)  

        driver= webdriver.Chrome(service=service,options=chrome_options)

        try:
            #https://mrbilit.com/buses/tehran-mashhad?departureDate=1403-12-20
            url= f"https://mrbilit.com/buses/{origin}-{destination}?adultCount=1&departureDate={date}"
            driver.get(url)

            time.sleep(10)




            buses= []                                         #سوال
            bus_elements=driver.find_elements(By.CLASS_NAME,'trip-card-container')
            for bus in bus_elements:
                  origin= bus.find_elements(By.CLASS_NAME,'location')[0].text.strip()
                  print(origin)
                  destination=bus.find_elements(By.CLASS_NAME,'location')[1].text.strip()
                  print(destination)
                  time_str=bus.find_elements(By.CLASS_NAME,'time-container')[0].text.strip()
                  print(time_str)
                  price=bus.find_elements(By.CLASS_NAME,'payable-price')[0].text.strip()
                  print(price)
                  capacity =bus.find_elements(By.CLASS_NAME, 'capacity-text')[0].text.strip()
                  print(capacity)
                  type_of_clases = bus.find_elements(By.CLASS_NAME, 'title')[0].text.strip()
                  print(type_of_clases)
                  print('-----------------------')

                  bus_data ={
                     "origin": origin,
                     "destination": destination,
                     "time": time_str,
                     "price": price,
                     "capacity": capacity,
                     "type_of_clases": type_of_clases,
                  }

                  buses.append(bus_data)
                  return buses

                  buses_json = json.dumps(buses,ensure_ascii=False,indent=4)

                  with open('flights.json', 'w', encoding='utf-8') as f:
                    f.write(buses_json)
                    
                    return buses_json
        finally:
             driver.quit()








def get_trains(date, origin, destination):
         
         chrome_options = Options()
         chrome_options.add_argument("--headless")  
         chrome_options.add_argument("--disable-gpu")  
         chrome_options.add_argument("--no-sandbox")  

         
         chromedriver_path = os.path.expanduser('C:\Users\fx506heb\Downloads\chromedriver-linux64\chromedriver-linux64')  # مسیر chromedriver در پوشه خانگی
         #chromedriver_path = 'chromedriver'
         service = Service(chromedriver_path)

         
        #  service = Service('C:\\Users\\fx506heb\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')  

         
         driver = webdriver.Chrome(service=service, options=chrome_options)

         try:
             
             url = f"https://www.mrbilit.com/trains/{origin}-{destination}?adultCount=1&departureDate={date}"
             driver.get(url)

             
             time.sleep(10)

             
             trains = []  
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

                 train_data = {
                     "origin": origin,
                     "destination": destination,
                     "time": time_str,
                     "price": price,
                     "capacity": capacity,
                     "type_of_clases": type_of_clases,
                 }
                

                 trains.append(train_data)
                 #return trains

                 trains_json = json.dumps(trains, ensure_ascii=False, indent=4)  

                 with open('flights.json', 'w', encoding='utf-8') as f:
                    f.write(trains_json)

                 return trains_json
             
         finally:
             
             driver.quit()








