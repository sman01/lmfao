from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import csv
from itertools import zip_longest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def err(url,no):
    if no<5:
        try:
            time.sleep(100)
            result = requests.get(url,headers=headers)
            print(result.status_code)
            print('why')
            return result.status_code
        except:
            print("error")
            time.sleep(150)
            return 2
            
    else:
        return 3


headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'}

companies=['Maruti_Suzuki', 'MG_Motor', 'Hyundai', 'Honda', 'Toyota', 'Mahindra', 'Tata', 'Kia', 'Volkswagen', 'Ford', 'Renault', 'BMW', 'Audi', 'Mercedes_Benz', 'Skoda', 'Datsun', 'Mitsubishi', 'Volvo', 'Nissan', 'Jaguar', 'Lamborghini', 'Rolls_Royce', 'MINI', 'Bugatti', 'Porsche', 'Ferrari', 'Land_Rover', 'Maserati', 'Bentley', 'ISUZU', 'Force_Motors', 'DC', 'Jeep', 'Aston_Martin', 'Lexus']

Maruti_Suzuki = ['Swift', 'Baleno', 'Vitara-Brezza', 'Dzire', 'Ertiga', 'Wagon-R', 'Alto-800', 'Celerio', 'S-Presso', 'S-Cross', 'XL6', 'Ignis', 'Ciaz', 'Eeco', 'Celerio-X', 'Swift-Dzire-Tour', 'Baleno-RS', 'Baleno-2014-2018', 'S-Cross-2017-2020', 'Vitara-Brezza-2016-2020', 'Dzire-2017-2020', 'Alto-K10', 'Wagon-R-[2001-2018]', 'Zen', 'Esteem', '800', 'Estilo', 'Ritz', 'A-Star', 'SX4', 'Omni', 'Gypsy']
MG_Motor = ['Hector', 'Gloster', 'ZS-EV', 'Hector-Plus', 'D90', 'Hector-2019-2021']
Hyundai = ['Creta', 'i20', 'Venue', 'Grand-i10', 'Verna', 'Aura', 'Santro', 'Tucson', 'Elantra', 'Kona-Electric', 'Grand-i10-Nios', 'Xcent-2020', 'Creta-2015-2020', 'Elantra-2015-2019', 'Verna-2017-2020', 'i20-Active', 'Elite-i20-2017-2020', 'Tucson-2016-2020', 'Xcent', 'EON', 'Santro-Xing', 'i10', 'Accent']
Honda = ['City', 'Amaze', 'Civic', 'Jazz', 'WR-V', 'CR-V', 'City-4th-Generation', 'Accord', 'Jazz-2018-2020', 'WRV-2017-2020', 'Brio', 'BRV', 'Mobilio', 'CR-V-[2009-2018]']
Toyota = ['Fortuner', 'Innova-Crysta', 'Glanza', 'Yaris', 'Vellfire', 'Camry', 'Urban-Cruiser', 'Tercel', 'Starlet', 'Sera', 'Premio', 'prado', 'Majesta', 'Estima', 'Cynos', 'Corona', 'Fortuner-2016-2021', 'Innova-Crysta-2016-2020', 'Camry', 'Etios-Liva', 'Platinum-Etios', 'Etios-Cross', 'Land-Cruiser', 'Qualis', 'Prius', 'Corolla-Altis', 'Land-Cruiser-Prado', 'Innova']
Mahindra = ['Thar', 'Scorpio', 'XUV300', 'Bolero', 'XUV500', 'Marazzo', 'TUV-300', 'KUV100-NXT', 'Alturas-G4', 'TUV-300-Plus', 'E-Verito', 'Bolero-Power-Plus', 'Bolero-Pik-Up', 'Marshal', 'Jeep', 'Supro', 'e2oPlus', 'NuvoSport', 'Armada', 'Verito-Vibe', 'e2o', 'Quanto', 'Bolero-2011-2019', 'Verito', 'Xylo', 'Logan', 'Thar-2015-2019']
Tata = ['Altroz', 'Harrier', 'Nexon', 'Tiago', 'Tigor', 'Yodha-Pickup', 'Tigor-EV', 'Nexon-EV', 'Tiago-2019-2020', 'Tigor-JTP', 'Tiago-JTP', 'Tiago-NRG', 'Hexa-2017-2020', 'Nexon-2017-2020', 'Tigor-2017-2020', 'Safari-Storme', 'Nano', 'Bolt', 'Zest', 'Indica-eV2', 'Sumo', 'Indigo-eCS', 'Manza', 'Vista', 'Safari-2005-2017', 'Indica']
Kia = ['Sonet', 'Seltos', 'Carnival']
Volkswagen = ['Polo', 'Vento', 'T-Roc', 'Tiguan-Allspace', 'Polo-GTI', 'Multivan', 'T-Cross', 'GTI', 'Vento-2015-2019', 'Polo-2015-2019', 'Tiguan', 'Passat', 'Ameo', 'Jetta', 'Touareg', 'Touareg']
Ford = ['EcoSport', 'Endeavour', 'Figo', 'Freestyle', 'Aspire', 'Endeavour-2015-2020', 'Mustang', 'Ecosport-2015-2021', 'Fiesta', 'Ikon']
Renault = ['KWID', 'Triber', 'Duster', 'Captur', 'Kaptur', 'Duster-2016-2019', 'KWID-2015-2019', 'Lodgy', 'Scala', 'Pulse', 'Fluence']
BMW = ['X1', 'X5', '3-Series', 'X6', 'X3', 'X7', '2-Series', '5-Series', 'Z4', '7-Series', 'M5', '6-Series', 'X4', 'M2', '8-Series', '3-Series-GT', 'X3-M', 'X5-M', 'X1-2015-2020', '3-Series-2015-2019', 'X6-2014-2019', '7-Series-2015-2019', 'M-Series', '1-Series']
Audi = ['A4', 'A6', 'Q2', 'Q8', 'A8', 'RS7', 'R8', 'GTI', 'RS-Q8', 'A2', 'S5', 'A4-2015-2020', 'A5', 'Q3', 'RS6-Avant', 'Q7', 'RS7-2015-2019', 'TT', 'A3-cabriolet', 'A3', 'S6', 'RS5', 'A8-2014-2019', 'Q5']
Mercedes_Benz = ['A-Class', 'E-Class', 'GLS', 'GLE', 'GLC', 'V-Class', 'G-Class', 'AMG-GLE-53', 'EQC', 'CLS', 'S-Class', 'AMG-GT', 'E-Class-All-Terrain', 'C-Class', 'AMG-GT-4-Door-Coupe', 'GLC-Coupe', 'Viano', 'MB-Class', 'GL-Class', 'G', 'CL-Class', 'GLA-Class', 'S-Class-Cabriolet', 'SLC', 'GLS-2016-2020', 'GLC-2016-2019', 'GLE-2015-2020', 'B-Class', 'GLA-45-AMG', 'CLA', 'AMG-GL', 'M-Class', 'SLS-AMG', 'R-Class', 'SLK', 'SL-Class', 'M-Class', 'CLK-Class']
Skoda = ['New-Rapid', 'New-Superb', 'Karoq', 'Octavia', 'Fabia', 'Laura', 'Kodiaq', 'Superb-2016-2020', 'Octavia-Combi', 'Yeti']
Datsun = ['redi-GO', 'GO', 'GO-Plus', 'redi-GO-2016-2020']
Mitsubishi = ['Pajero-Sport', 'FTO', 'Challenger', 'Outlander', 'EVO-XI', 'Lancer-Evolution-X', 'Montero', 'Lancer', 'Cedia']
Volvo = ['XC90', 'XC40', 'S90', 'XC60', 'V90-Cross-Country', 'S40', 'S60-Cross-Country', 'V40', 'S60', 'V40-Cross-Country', 'S80']
Nissan = ['Magnite', 'Kicks', 'GT-R', 'Urvan', 'Primera', 'Jonga', 'Gloria', '350Z', 'Micra-Active', 'Terrano', 'Evalia', 'Sunny', '370Z', 'Micra', 'Teana']
Jaguar = ['F-PACE', 'XE', 'F-TYPE', 'XF', 'XJ', 'XE-2016-2019', 'F-TYPE-2013-2020', 'XK']
Lamborghini = ['Urus', 'Aventador', 'Huracan-EVO', 'Huracan', 'Murcielago', 'Gallardo']
Rolls_Royce = ['Phantom', 'Ghost', 'Wraith', 'Cullinan', 'Dawn', 'Drophead', 'Ghost-2009-2020']
MINI = ['Countryman', 'Cooper-Convertible', 'Cooper-3-DOOR', 'Clubman', 'Cooper-5-DOOR', 'Cooper']
Bugatti = ['Chiron', 'Divo', 'Veyron']
Porsche = ['Macan', '911', 'Panamera', 'Cayenne', '718', 'Cayenne-Coupe', 'Carrera-GT', 'Macan-2013-2019', 'Cayman', 'Boxster', '911-2016-2019']
Ferrari = ['Portofino', 'Roma', 'SF90-Stradale', 'GTC4Lusso', '812', 'F8-Tributo', '812-Superfast', 'F620-GT', 'F430', 'Enzo', '612', '575-Superamerica', '458-Spider', '458-Speciale', '458', '488', 'California-T', 'FF', '599-GTB-Fiorano', '458-Italia']
Land_Rover = ['Range-Rover', 'Range-Rover-Velar', 'Defender', 'Range-Rover-Evoque', 'Discovery', 'Range-Rover-Sport', 'Discovery-Sport', 'Range-Rover-2010-2012', 'Discovery-3', 'Range-Rover-Evoque-2016-2020', 'Discovery-Sport-2015-2020', 'Freelander-2', 'Discovery-4']
Maserati = ['Levante', 'Quattroporte', 'Ghibli', 'GranTurismo', 'GranCabrio']
Bentley = ['Continental', 'Mulsanne', 'Flying-Spur', 'Bentayga', 'Brookland', 'Azure', 'Arnage']
ISUZU = ['MUX', 'D-Max-V-Cross', 'D-Max', 'D-MAX-V-Cross-2015-2019', 'MU-7']
Force_Motors = ['Trax-Cruiser', 'Gurkha', 'One']
DC = ['Avanti']
Jeep = ['Compass', 'Wrangler', 'Compass-Trailhawk', 'Wrangler-2016-2019', 'Grand-Cherokee']
Aston_Martin = ['Vantage', 'DB11', 'Virage', 'One-77', 'Vantage-2011-2019', 'Vanquish', 'DB11-2016-2020', 'Rapide', 'DB9']
Lexus = ['LS', 'ES', 'NX', 'LX', 'RX', 'LC-500h']