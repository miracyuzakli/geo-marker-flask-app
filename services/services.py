from seleniumwire import webdriver
import time
import pandas as pd
import requests
import sys
import csv
import requests
import json
# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from geopy.distance import geodesic
from geopy.point import Point
import numpy as np
import os
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options





# def scrape_function(city, city_name, sale_date, property_type, price_amount, lot_size, coordinates):

    
#     if sale_date == '30 days':
#         last_date = 30
#     elif sale_date == '3 Months':
#         last_date = 90
#     elif sale_date == '6 Months':
#         last_date = 180
#     else:
#         last_date = 365
    
#     with open(os.path.join("services", 'cookie.txt'),'r',encoding='utf-8') as file:
#         cookie = file.read()
   

#     url = "https://collaboration.geowarehouse.ca/gema-rest/rest/comparableSales/circle?sort=area&direction=asc"

#     headers = {
#             'Cookie': cookie,
#             'Content-Type': 'application/json'
#         }

#     response = requests.request("POST", url, headers=headers)#, data=payload

#     if response.status_code != 200:

#         chrome_options = Options()
#         chrome_options.add_experimental_option("detach", True)
#         driver = webdriver.Chrome(options=chrome_options)


        
        
        
#         driver.get('https://treb.clareityiam.net/idp/login')
#         time.sleep(60)
#         time.sleep(3)                                                                     

#         driver.get('https://communications.torontomls.net/mlshome/redirect/mlschoice.php')
#         try:
#             wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , '//*[@id="btnContinue"]')))
#             continue_button = driver.find_element(By.XPATH,value='//*[@id="btnContinue"]').get_attribute('href')
#             driver.get(continue_button)
#         except:
#             pass
        
#         time.sleep(20)

#         driver.get('https://trreb.mlxmatrix.com/Matrix/Tools')
#         time.sleep(20)

#         driver.get('https://trreb.mlxmatrix.com/Matrix/special/thirdpartyformpost.aspx?n=GeoWarehouse')

#         time.sleep(20)


#         print('yazdır')

#         try:
#             search_button = driver.find_element(By.XPATH,value ='//*[@id="searchTextBox"]').click()
#         except:
#             print('151 patladı tıklamadı')
#             time.sleep(4)                                                       

#         time.sleep(5) 
#         cookie = ''

#         for request in driver.requests:
#             if 'search' in request.path:
                
#                 headers = request.headers
#                 cookie = headers.get("Cookie")
#                 break
#         print('Line 175',cookie)

#         with open(os.path.join("services", 'cookie.txt'),'w') as file:
#             file.write(cookie)
        
#         print(coordinates)

#         with open(os.path.join("services", 'cookie.txt'),'r') as file:
#             cookie = file.read()

#     region_to_lro = {
#                 "Algoma": "01",
#                 "Brant": "02",
#                 "Bruce": "03",
#                 "Cochrane": "06",
#                 "Dufferin": "07",
#                 "Dundas": "08",
#                 "Durham": "40",
#                 "Elgin": "11",
#                 "Essex": "12",
#                 "Frontenac": "13",
#                 "Glengarry": "14",
#                 "Grenville": "15",
#                 "Grey": "16",
#                 "Haldimand": "18",
#                 "Haliburton": "19",
#                 "Halton": "20",
#                 "Hamilton": "62",
#                 "Hastings": "21",
#                 "Huron": "22",
#                 "Kenora": "23",
#                 "Kent": "24",
#                 "Lambton": "25",
#                 "Lanark": "27",
#                 "Leeds": "28",
#                 "Lennox": "29",
#                 "Manitoulin": "31",
#                 "Middlesex": "33",
#                 "Muskoka": "35",
#                 "Niagara North": "30",
#                 "Niagara South": "59",
#                 "Nipissing": "36",
#                 "Norfolk": "37",
#                 "Northumberland": "39",
#                 "Ottawa-Carleton": "04",
#                 "Oxford": "41",
#                 "Parry": "42",
#                 "Peel": "43",
#                 "Perth": "44",
#                 "Peterborough": "45",
#                 "Prescott": "46",
#                 "Prince": "47",
#                 "Rainy": "48",
#                 "Renfrew": "49",
#                 "Russell": "50",
#                 "Simcoe": "51",
#                 "Stormont": "52",
#                 "Sudbury": "53",
#                 "Thunder": "55",
#                 "Timiskaming": "54",
#                 "Toronto": "80",
#                 "Victoria": "57",
#                 "Waterloo": "58",
#                 "Wellington": "61",
#                 "York": "65"
#             }
    

#     latitudes = [coord[0] for coord in coordinates]
#     longitudes = [coord[1] for coord in coordinates]
#     min_lat, max_lat = min(latitudes), max(latitudes)
#     min_lon, max_lon = min(longitudes), max(longitudes)

#     results = {}

#     step = 0.01
#     for lat in np.arange(min_lat, max_lat, step):
#         for lon in np.arange(min_lon, max_lon, step):
#             central_point = (lat, lon)

#             # Yarıçap içindeki noktaları kontrol et
#             for angle in range(0, 360, 10):
#                 new_point = geodesic(kilometers=1).destination(central_point, angle)
#                 new_lat, new_lon = new_point.latitude, new_point.longitude

#                 if min_lat <= new_lat <= max_lat and min_lon <= new_lon <= max_lon:
#                     key = f"{new_lat}-{new_lon}"
#                     results[key] = [new_lat, new_lon]

#     print(len(results))

#     url = "https://collaboration.geowarehouse.ca/gema-rest/rest/comparableSales/circle?sort=area&direction=asc"

#     area_list = list()
#     condo_list = list()
#     considerationAmount_list = list()
#     distance_list = list()
#     pin_list = list()
#     registrationDate_list = list()
#     yearBuilt_list = list()
#     propertyCode_list = list()
#     rollNumber_list = list()
#     streetViewUrl_list = list()
#     teranetPropertyType_list = list()
#     areaInAcres_list = list()
#     id_list = list()
#     lro_list = list()
#     useAcres_list = list()
#     saleAddressStr_list = list()

#     min_price = price_amount.get('from')
#     min_price = min_price.replace('$','')
#     max_price = price_amount.get('to')
#     max_price = max_price.replace('$','')
#     city_value = region_to_lro.get(city_name)
#     for key,value in results.items():
        
#         latitude = value[0]
#         longitude = value[1]
#         if property_type == 'Freehold':
#             payload = json.dumps({
#                 "center": {
#                 "latitude": latitude,
#                 "longitude": longitude
#                 },
#                 "radiusInMeters": 1000,
#                 "lastDays": last_date,
#                 "minAmount": int(min_price),
#                 "maxAmount": int(max_price),
#                 "condo": False,
#                 "saveAsDefault": True,
#                 "maxArea": "199507673.257241",
#                 "minArea": "0",
#                 "freehold": True,
#                 "mps": False,
#                 "lro": int(city_value)
#             })
#         elif property_type == 'Condo':
#             payload = json.dumps({
#                 "center": {
#                 "latitude": latitude,
#                 "longitude": longitude
#                 },
#                 "radiusInMeters": 1000,
#                 "lastDays": last_date,
#                 "minAmount": int(min_price),
#                 "maxAmount": int(max_price),
#                 "condo": True,
#                 "saveAsDefault": True,
#                 "maxArea": "199507673.257241",
#                 "minArea": "0",
#                 "freehold": False,
#                 "mps": False,
#                 "lro": int(city_value)
#             })
#         else:
#             payload = json.dumps({
#                 "center": {
#                 "latitude": latitude,
#                 "longitude": longitude
#                 },
#                 "radiusInMeters": 1000,
#                 "lastDays": last_date,
#                 "minAmount": int(min_price),
#                 "maxAmount": int(max_price),
#                 "condo": True,
#                 "saveAsDefault": True,
#                 "maxArea": "199507673.257241",
#                 "minArea": "0",
#                 "freehold": True,
#                 "mps": False,
#                 "lro": int(city_value)
#             })

#         headers = {
#             'Cookie': cookie,
#             'Content-Type': 'application/json'
#         }

#         response = requests.request("POST", url, headers=headers, data=payload)
#         if len(response.json()['sales']) > 0:
#             for item in range(len(response.json()['sales'])):
#                 print('Line 224 Total Found ',len(response.json()['sales']))
#                 value = response.json()['sales'][item]
#                 area_list.append(value['area'])
#                 condo_list.append(value['condo'])
#                 considerationAmount_list.append(value['considerationAmount'])
#                 distance_list.append(value['distance'])
#                 pin_list.append(value['pin'])
#                 registrationDate_list.append(value['registrationDate'])
#                 yearBuilt_list.append(value['yearBuilt'])
#                 propertyCode_list.append(value['propertyCode'])
#                 rollNumber_list.append(value['rollNumber'])
#                 streetViewUrl_list.append(value['streetViewUrl'])
#                 teranetPropertyType_list.append(value['teranetPropertyType'])
#                 areaInAcres_list.append(value['areaInAcres'])
#                 id_list.append(value['id'])
#                 lro_list.append(value['lro'])
#                 useAcres_list.append(value['useAcres'])
#                 saleAddressStr_list.append(value['saleAddressStr'])
#         else:       
#             pass

#     result_dataframe = pd.DataFrame()
#     result_dataframe['Area'] = area_list
#     result_dataframe['Condo'] = condo_list
#     result_dataframe['Consideration Amount'] = considerationAmount_list
#     result_dataframe['Distance (KM)'] = distance_list
#     result_dataframe['PIN'] = pin_list
#     result_dataframe['Registration Date'] = registrationDate_list
#     result_dataframe['ID'] = id_list
#     result_dataframe['Area In Acres'] = areaInAcres_list
#     result_dataframe['LRO Number'] = lro_list
#     result_dataframe['Use Acres'] = useAcres_list
#     result_dataframe['Sale Address'] = saleAddressStr_list

#     result_dataframe.drop_duplicates(subset='PIN',keep='first')

#     result_dataframe.to_excel('Area_Scraping_Results.xlsx',index=False)

#     return True






















from seleniumwire import webdriver
import time
import pandas as pd
import requests
import sys
import csv
import requests
import json
# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from geopy.distance import geodesic
from geopy.point import Point
import numpy as np
import os
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options






class GeoWarehouseScraper:


    def __init__(self) -> None:
        self.region_to_lro = {
                "Algoma": "01",
                "Brant": "02",
                "Bruce": "03",
                "Cochrane": "06",
                "Dufferin": "07",
                "Dundas": "08",
                "Durham": "40",
                "Elgin": "11",
                "Essex": "12",
                "Frontenac": "13",
                "Glengarry": "14",
                "Grenville": "15",
                "Grey": "16",
                "Haldimand": "18",
                "Haliburton": "19",
                "Halton": "20",
                "Hamilton": "62",
                "Hastings": "21",
                "Huron": "22",
                "Kenora": "23",
                "Kent": "24",
                "Lambton": "25",
                "Lanark": "27",
                "Leeds": "28",
                "Lennox": "29",
                "Manitoulin": "31",
                "Middlesex": "33",
                "Muskoka": "35",
                "Niagara North": "30",
                "Niagara South": "59",
                "Nipissing": "36",
                "Norfolk": "37",
                "Northumberland": "39",
                "Ottawa-Carleton": "04",
                "Oxford": "41",
                "Parry": "42",
                "Peel": "43",
                "Perth": "44",
                "Peterborough": "45",
                "Prescott": "46",
                "Prince": "47",
                "Rainy": "48",
                "Renfrew": "49",
                "Russell": "50",
                "Simcoe": "51",
                "Stormont": "52",
                "Sudbury": "53",
                "Thunder": "55",
                "Timiskaming": "54",
                "Toronto": "80",
                "Victoria": "57",
                "Waterloo": "58",
                "Wellington": "61",
                "York": "65"
            }

        with open(os.path.join("services", 'cookie.txt'),'r',encoding='utf-8') as file:
            self.cookie = file.read()

        
        self.get_cookies()

    def get_cookies(self):

        print("get_cookies function started for cookies")

        url = "https://collaboration.geowarehouse.ca/gema-rest/rest/comparableSales/circle?sort=area&direction=asc"

        headers = {
                'Cookie': self.cookie,
                'Content-Type': 'application/json'
            }

        response = requests.request("POST", url, headers=headers)#, data=payload

        if response.status_code != 200:

            chrome_options = Options()
            chrome_options.add_experimental_option("detach", True)
            driver = webdriver.Chrome(options=chrome_options)


            
            
            
            driver.get('https://treb.clareityiam.net/idp/login')
            time.sleep(60)
            time.sleep(3)                                                                     

            driver.get('https://communications.torontomls.net/mlshome/redirect/mlschoice.php')
            try:
                wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , '//*[@id="btnContinue"]')))
                continue_button = driver.find_element(By.XPATH,value='//*[@id="btnContinue"]').get_attribute('href')
                driver.get(continue_button)
            except:
                pass
            
            time.sleep(20)

            driver.get('https://trreb.mlxmatrix.com/Matrix/Tools')
            time.sleep(20)

            driver.get('https://trreb.mlxmatrix.com/Matrix/special/thirdpartyformpost.aspx?n=GeoWarehouse')

            time.sleep(20)


            print('yazdır')

            try:
                search_button = driver.find_element(By.XPATH,value ='//*[@id="searchTextBox"]').click()
            except:
                print('151 patladı tıklamadı')
                time.sleep(4)                                                       

            time.sleep(5) 
            self.cookie = ''

            for request in driver.requests:
                if 'search' in request.path:
                    
                    headers = request.headers
                    self.cookie = headers.get("Cookie")
                    break
            print('Line 175',self.cookie)

            with open(os.path.join("services", 'cookie.txt'),'w') as file:
                file.write(self.cookie)
            
            with open(os.path.join("services", 'cookie.txt'),'r') as file:
                self.cookie = file.read()


            print("get_cookies function finished")
            return True
        



    def run_scrabe(self, city, city_name, sale_date, property_type, price_amount, lot_size, coordinates):

        if sale_date == '30 days':
            last_date = 30
        elif sale_date == '3 Months':
            last_date = 90
        elif sale_date == '6 Months':
            last_date = 180
        else:
            last_date = 365
        
        latitudes = [coord[0] for coord in coordinates]
        longitudes = [coord[1] for coord in coordinates]
        min_lat, max_lat = min(latitudes), max(latitudes)
        min_lon, max_lon = min(longitudes), max(longitudes)

        results = {}

        step = 0.01
        for lat in np.arange(min_lat, max_lat, step):
            for lon in np.arange(min_lon, max_lon, step):
                central_point = (lat, lon)

                # Yarıçap içindeki noktaları kontrol et
                for angle in range(0, 360, 10):
                    new_point = geodesic(kilometers=1).destination(central_point, angle)
                    new_lat, new_lon = new_point.latitude, new_point.longitude

                    if min_lat <= new_lat <= max_lat and min_lon <= new_lon <= max_lon:
                        key = f"{new_lat}-{new_lon}"
                        results[key] = [new_lat, new_lon]

        print(len(results))

        url = "https://collaboration.geowarehouse.ca/gema-rest/rest/comparableSales/circle?sort=area&direction=asc"

        area_list = list()
        condo_list = list()
        considerationAmount_list = list()
        distance_list = list()
        pin_list = list()
        registrationDate_list = list()
        yearBuilt_list = list()
        propertyCode_list = list()
        rollNumber_list = list()
        streetViewUrl_list = list()
        teranetPropertyType_list = list()
        areaInAcres_list = list()
        id_list = list()
        lro_list = list()
        useAcres_list = list()
        saleAddressStr_list = list()

        min_price = price_amount.get('from')
        min_price = min_price.replace('$','')
        max_price = price_amount.get('to')
        max_price = max_price.replace('$','')
        city_value = self.region_to_lro.get(city_name)
        for key,value in results.items():
            
            latitude = value[0]
            longitude = value[1]
            if property_type == 'Freehold':
                payload = json.dumps({
                    "center": {
                    "latitude": latitude,
                    "longitude": longitude
                    },
                    "radiusInMeters": 1000,
                    "lastDays": last_date,
                    "minAmount": int(min_price),
                    "maxAmount": int(max_price),
                    "condo": False,
                    "saveAsDefault": True,
                    "maxArea": "199507673.257241",
                    "minArea": "0",
                    "freehold": True,
                    "mps": False,
                    "lro": int(city_value)
                })
            elif property_type == 'Condo':
                payload = json.dumps({
                    "center": {
                    "latitude": latitude,
                    "longitude": longitude
                    },
                    "radiusInMeters": 1000,
                    "lastDays": last_date,
                    "minAmount": int(min_price),
                    "maxAmount": int(max_price),
                    "condo": True,
                    "saveAsDefault": True,
                    "maxArea": "199507673.257241",
                    "minArea": "0",
                    "freehold": False,
                    "mps": False,
                    "lro": int(city_value)
                })
            else:
                payload = json.dumps({
                    "center": {
                    "latitude": latitude,
                    "longitude": longitude
                    },
                    "radiusInMeters": 1000,
                    "lastDays": last_date,
                    "minAmount": int(min_price),
                    "maxAmount": int(max_price),
                    "condo": True,
                    "saveAsDefault": True,
                    "maxArea": "199507673.257241",
                    "minArea": "0",
                    "freehold": True,
                    "mps": False,
                    "lro": int(city_value)
                })

            headers = {
                'Cookie': self.cookie,
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            if len(response.json()['sales']) > 0:
                for item in range(len(response.json()['sales'])):
                    print('Line 224 Total Found ',len(response.json()['sales']))
                    value = response.json()['sales'][item]
                    area_list.append(value['area'])
                    condo_list.append(value['condo'])
                    considerationAmount_list.append(value['considerationAmount'])
                    distance_list.append(value['distance'])
                    pin_list.append(value['pin'])
                    registrationDate_list.append(value['registrationDate'])
                    yearBuilt_list.append(value['yearBuilt'])
                    propertyCode_list.append(value['propertyCode'])
                    rollNumber_list.append(value['rollNumber'])
                    streetViewUrl_list.append(value['streetViewUrl'])
                    teranetPropertyType_list.append(value['teranetPropertyType'])
                    areaInAcres_list.append(value['areaInAcres'])
                    id_list.append(value['id'])
                    lro_list.append(value['lro'])
                    useAcres_list.append(value['useAcres'])
                    saleAddressStr_list.append(value['saleAddressStr'])
            else:       
                pass

        result_dataframe = pd.DataFrame()
        result_dataframe['Area'] = area_list
        result_dataframe['Condo'] = condo_list
        result_dataframe['Consideration Amount'] = considerationAmount_list
        result_dataframe['Distance (KM)'] = distance_list
        result_dataframe['PIN'] = pin_list
        result_dataframe['Registration Date'] = registrationDate_list
        result_dataframe['ID'] = id_list
        result_dataframe['Area In Acres'] = areaInAcres_list
        result_dataframe['LRO Number'] = lro_list
        result_dataframe['Use Acres'] = useAcres_list
        result_dataframe['Sale Address'] = saleAddressStr_list

        result_dataframe.drop_duplicates(subset='PIN',keep='first')

        result_dataframe.to_excel('Area_Scraping_Results.xlsx',index=False)

        return True





