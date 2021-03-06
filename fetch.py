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


url = []
companies = [
    "Hero_Moto_Corp",
    "Honda",
    "Royal_Enfield",
    "Yamaha",
    "Bajaj",
    "TVS",
    "Jawa_Motorcycles",
    "KTM",
    "Suzuki",
    "Revolt_Motors",
    "CFMoto",
    "rem22Kymco",
    "Vespa",
    "Kawasaki",
    "Harley_Davidson",
    "Ducati",
    "Triumph",
    "BMW",
    "Benelli",
    "Husqvarna",
    "YObykes",
    "Palatino",
    "Okinawa",
    "MV_Agusta",
    "Lohia",
    "Li_ions_Elektrik_Solutions",
    "Lectro_Electric",
    "Essel_Energy",
    "BGauss",
    "Avon",
    "Ather_Energy",
    "Ampere",
    "Aftek_Motors",
    "Hero_Electric",
    "Mahindra",
    "Indian",
    "Moto_Guzzi",
    "Aprilia",
]

Hero_Moto_Corp = [
    "Splendor-Plus",
    "HF-Deluxe",
    "Passion-Pro",
    "Pleasure-Plus",
    "Super-Splendor",
    "Glamour",
    "Xtreme-160R",
    "XPulse-200",
    "Maestro-Edge-125",
    "Xtreme-200S",
    "Splendor-iSmart",
    "Destini-125",
    "Maestro-Edge-110-BS6",
    "CBZ",
    "Splendor-iSmart-BS4",
    "Karizma-ZMR",
    "Duet",
    "Maestro-Edge-BS4",
    "Xtreme-Sports",
    "Splendor-PRO",
    "HF-Dawn",
    "Passion-XPro",
    "HF-Deluxe-BS4",
    "Pleasure",
    "Passion-Pro-BS4",
    "Impulse",
    "Hunk",
    "Achiever",
]
Honda = [
    "Activa-6G",
    "Shine",
    "Dio",
    "Activa-125",
    "Hness-CB350",
    "SP-125",
    "Unicorn",
    "Hornet-2.0",
    "Livo",
    "XBlade",
    "Grazia",
    "CD-110-Dream",
    "Gold-Wing",
    "CRF1100L-Africa-Twin",
    "Gold-Wing-BS4",
    "CBR650R-BS4",
    "CBR300R-BS4",
    "CB300R-BS4",
    "Honda-CB1000R-Plus-BS4",
    "CB-Hornet-160R-BS4",
    "CBR250R",
    "Activa-5G",
    "XBlade-BS4",
    "Grazia-BS4",
    "Cliq",
    "CRF1000L-Africa-Twin",
    "Navi",
    "CB-Shine-SP",
    "Livo-BS4",
    "Aviator",
    "Activa-i",
    "Activa-4G",
    "CBR650F",
    "CB-Unicorn-160",
    "CD-110-Dream-BS4",
    "Activa-125-BS4",
    "Dream-Neo",
    "Dream-Yuga",
    "Dio-BS4",
    "CBR1000RR",
    "CB-Unicorn-150",
    "CB-Shine-BS4",
    "CB1000R",
]
Royal_Enfield = [
    "Classic-350",
    "Bullet-350",
    "Meteor-350",
    "Himalayan",
    "Interceptor-650",
    "Continental-GT-650",
    "Bullet-Trials-500",
    "Bullet-Trials-350",
    "Thunderbird-350X",
    "Thunderbird-500X",
    "Himalayan-BS4",
    "Bullet-500",
    "Thunderbird-350",
    "Thunderbird-500",
    "Classic-500",
    "Continental-GT",
]
Yamaha = [
    "YZF-R15-V3",
    "MT-15",
    "Fascino-125",
    "FZS-FI-V3",
    "RayZR-125",
    "FZ-FI-Version-3.0",
    "FZ-25",
    "YZF-R1M",
    "FZS-25",
    "FZ-25-BS4",
    "Fazer-153",
    "YZF-R125",
    "FZ-S-Fi-Version-3.0-BS4",
    "RX-135",
    "RX-100",
    "YZF-R3",
    "Fazer-25",
    "Saluto-RX",
    "Ray-ZR",
    "MT-09(2016-2020)",
    "YZF-R15S",
    "Fascino",
    "Saluto",
    "Alpha",
    "SZ-RR",
    "FZ-S-FI-(V-2.0)",
    "Ray-Z",
    "Gladiator",
    "FZ-FI",
    "Fazer-FI",
]
Bajaj = [
    "Pulsar-150",
    "Pulsar-NS200",
    "Pulsar-125-Neon",
    "Pulsar-220-F",
    "Pulsar-RS200",
    "Pulsar-NS160",
    "CT-100",
    "Dominar-400",
    "Platina-100",
    "Chetak",
    "Avenger-Cruise-220",
    "Avenger-Street-160",
    "Dominar-250",
    "Platina-110-H-Gear",
    "CT110",
    "Pulsar-180F",
    "Pulsar-150(2009-2014)",
    "Avenger-Street-220-BS4",
    "Avenger-Street-180",
    "Discover-110",
    "V12",
    "V15-Power-Up",
    "Discover-125",
    "Platina-110",
    "Pulsar-135LS",
    "Pulsar-180",
    "Boxer",
]
TVS = [
    "Apache-RTR-160",
    "Apache-RTR-160-4V",
    "Apache-RTR-200-4V",
    "Apache-RR-310",
    "Apache-RTR-180",
    "Jupiter",
    "NTORQ-125",
    "XL100",
    "Sport",
    "Radeon",
    "Scooty-Pep-Plus",
    "Star-City-Plus",
    "Scooty-Zest",
    "iQube-Electric",
    "Star",
    "Star-City-Plus-BS4",
    "Velocity",
    "Jupiter-Grande",
    "Scooty-Streak",
    "Wego",
]
Jawa_Motorcycles = ["Perak", "42", "Jawa"]
KTM = [
    "200-Duke",
    "125-Duke",
    "390-Duke",
    "RC-200",
    "RC-125",
    "RC-390",
    "250-Duke",
    "390-Adventure",
    "250-Adventure",
    "1050-Adventure",
]
Suzuki = [
    "Access-125",
    "Gixxer",
    "Gixxer-SF",
    "Burgman-Street",
    "Intruder",
    "Gixxer-SF-250",
    "Gixxer-250",
    "V-Strom-650XT",
    "Gixxer-SF-250-BS4",
    "Gixxer-250-BS4",
    "Access-125-BS4",
    "GSX-S1000F",
    "Gixxer-SF-(2015-2018)",
    "Gixxer-(2014-2018)",
    "V-Strom-1000",
    "Hayate",
]
Revolt_Motors = ["RV400", "RV300"]
CFMoto = [
    "300NK",
    "650MT",
    "650NK",
    "650GT",
    "650NK-BS4",
    "650MT-BS4",
    "650GT-BS4",
    "300NK-BS4",
]
rem22Kymco = ["Flow", "iFlow"]
Vespa = [
    "VXL-150",
    "SXL-125",
    "Notte-125",
    "VXL-125",
    "LX-125",
    "SXL-150",
    "Elegante-150",
    "ZX-125",
    "Urban-Club-125",
    "Connectivity",
    "RED-125",
    "946-Emporio-Armani-Edition",
    "SXL-150-BS4",
    "Elegante-125",
]
Kawasaki = [
    "Ninja-1000SX",
    "Z900",
    "Vulcan-S",
    "Z-H2",
    "KLX-140",
    "Z650",
    "Versys-650",
    "KLX-110",
    "KX-100",
    "KX-250",
    "KX-450F",
    "KLX-450R",
    "Versys-1000",
    "W800-Street",
    "Ninja-650",
    "Z900RS-BS4",
    "Z1000-BS4",
    "W800-Street-BS4",
    "Vulcan-S-BS4",
    "Versys-X-300-BS4",
    "Versys-650-BS4",
    "Kawasaki-Versys-1000-BS4",
    "Ninja-ZX-6R-BS4",
    "Ninja-ZX-10R-BS4",
    "Ninja-ZX-14R-BS4",
    "Ninja-H2-SX-BS4",
    "Ninja-H2-BS4",
    "Ninja-400-BS4",
    "Ninja-300-BS4",
    "Ninja-1000-BS4",
    "Ninja-ZX-10RR",
    "Ninja-650-(2011-2020)",
    "Z900-(2018-2020)",
    "Z650-(2017-2020)",
    "Versys-1000-(2014-2018)",
    "ER---6n",
    "Eliminator",
    "Z250",
    "Z800",
]
Harley_Davidson = [
    "Iron-883",
    "Street-750",
    "Fat-Boy",
    "Forty-Eight",
    "Street-Rod",
    "1200-Custom",
    "Road-King",
    "Low-Rider",
    "Forty-Eight-Special",
    "Low-Rider-S",
    "Iron-1200",
    "Harley-Davidson-Dyna",
    "FXDC-SUPER-GLIDE",
    "Fat-Boy-Anniversary",
    "Deluxe",
    "Fat-Bob",
    "Heritage-Classic",
    "Road-Glide-Special",
    "Street-Bob",
    "Street-Glide-Special",
    "Roadster",
    "CVO-Limited",
    "DYNA",
    "SOFTAIL",
]
Ducati = [
    "Scrambler-800",
    "Panigale-V2",
    "Scrambler-1100",
    "Multistrada-950",
    "XDiavel-BS4",
    "SuperSport-BS4",
    "Scrambler-Desert-Sled-BS",
    "Scrambler-1100-BS4",
    "Scrambler-BS4",
    "Panigale-V4-BS4",
    "Multistrada-950-BS4",
    "Multistrada-1260-BS4",
    "Monster-821-BS4",
    "Monster-797-BS4",
    "Hypermotard-950-BS4",
    "Diavel-1260-BS4",
    "Hyperstrada",
    "1199-Panigale",
    "Monster-1200-S-Stripe",
    "Monster-1200-S",
    "Monster-796",
    "1198",
    "Monster-821-Dark",
    "Monster-795",
    "Panigale-R",
    "1299-Panigale-S",
    "Diavel-Diesel",
    "1299-Superleggera",
    "959-Panigale",
    "Monster-1200",
    "1299-Panigale",
    "Panigale",
    "899-Panigale",
    "Streetfighter",
    "848",
    "Multistrada",
    "Hypermotard-939",
    "Diavel",
]
Triumph = [
    "Rocket-3",
    "Bonneville-T120",
    "Street-Triple",
    "Street-Twin",
    "Bonneville-T100",
    "Thunderbird-LT",
    "Bonneville-Speedmaster",
    "Tiger-900",
    "Tiger-Sport",
    "Rocket-III",
    "Tiger-800",
    "Tiger-Explorer",
    "Daytona-675",
    "Speed-Triple",
    "2017-Thruxton",
]
BMW = [
    "G-310-R",
    "S-1000-RR",
    "G-310-GS",
    "R-1250-GS",
    "R-1250-GS-Adventure",
    "F-900-R",
    "F-900-XR",
    "R-1250-RT",
    "R-1250-R",
    "S-1000-XR",
    "R-18",
    "F-850-GS-BS4",
    "F-750-GS-BS4",
    "S-1000-RR-BS4",
    "R-NineT-Scrambler-BS4",
    "BMW-R-NineT-Racer-BS4",
    "BMW-R-nineT-BS4",
    "BMW-R-1250-RT",
    "R-1250-R-BS4",
    "BMW-R-1250-GS-Adventure-BS4",
    "BMW-R-1250-GS-BS4",
    "BMW-K-1600-GTL-BS4",
    "BMW-K-1600-B-BS4",
    "BMW-G-310-R-BS4",
    "HP2-Sport",
    "BMW-K1300S",
    "R-1200-RS",
    "R-1200-RT",
    "R-1200-GS-Adventure",
    "R-1200-R",
    "S-1000-XR-(2017-2020)",
    "S-1000-R",
    "BMW-F700",
    "BMW-F650",
    "K-1300-R",
    "R-1200-GS",
]
Benelli = [
    "Imperiale-400",
    "BMW-G-310-GS-BS4",
    "TRK-502-BS4",
    "TNT-600i-BS4",
    "TNT-300-BS4",
    "Leoncino-500-BS4",
    "Leoncino-250-BS4",
    "302R-BS4",
    "Trek-1130",
    "TNT-25",
    "TNT-899",
    "TNT-600-GT",
    "TNT-R",
]
Husqvarna = ["Vitpilen-250", "Svartpilen-250"]
YObykes = ["Drift", "Edge"]
Palatino = ["Angel", "Sunshine", "Princess", "Spyker", "Ryan"]
Okinawa = [
    "Praise",
    "i-Praise",
    "PraisePro",
    "R30-electric-scooter",
    "Lite",
    "Ridge",
    "Raise",
    "Dual",
]
MV_Agusta = ["Brutale-1090", "F4", "F3", "Brutale"]
Lohia = ["Oma-Star", "Oma-Star-Li", "Elit-3000", "Genius", "Fame"]
Li_ions_Elektrik_Solutions = ["Spock-Electric-Scooter"]
Lectro_Electric = [
    "E-Zephyr-TX",
    "Essentia-TX",
    "Glide-TX",
    "E-Zephyr",
    "Glide-Unisex",
    "Glide-Lady",
    "Essentia",
    "Townmaster",
    "EHX20",
]
Essel_Energy = ["GET-7", "GET-1"]
BGauss = ["B8", "A2"]
Avon = [
    "E-Scoot",
    "E-Plus",
    "E-Lite",
    "E-Mate",
    "E-Star",
    "Avon-E-Bike-VX",
    "E-Magic",
    "E-Bike",
]
Ather_Energy = ["450X", "450", "340"]
Ampere = ["Reo", "V48", "Zeal", "Reo-Elite", "Magnus"]
Aftek_Motors = ["Scorpion", "Royal-Plus", "Skipper", "Turbo-170"]
Hero_Electric = [
    "Optima-LA",
    "Flash",
    "NYX",
    "Optima-HS500-ER",
    "Dash",
    "Photon",
    "Optima-E5",
    "Optima-Li",
    "Photon-48V",
    "Hero-Electric-Zion",
    "Hero-Electric-Zippy",
    "Optima-DX",
    "Optima-Plus",
    "Cruz",
    "Wave",
    "Maxi",
    "E-Sprint",
    "Avior-E-Cycle",
]
Mahindra = [
    "Mojo-300-BS6",
    "Mojo-300-BS4",
    "MOJO-UT-300",
    "Genze-2.0",
    "Gusto-125",
    "MOJO-XT-300",
    "Gusto",
    "Stallio",
    "Centuro",
    "Pantero",
    "SYM-Flyte",
    "Duro",
    "Rodeo",
    "kine",
]
Indian = [
    "Springfield-Dark-Horse",
    "Springfield-Dark-Horse-BS4",
    "Springfield-BS4",
    "Scout-Sixty-BS4",
    "Scout-Bobber-BS4",
    "scout-BS4",
    "Roadmaster-Elite-BS4",
    "Roadmaster-Classic-BS4",
    "Roadmaster-BS4",
    "FTR-1200-BS4",
    "Chieftain-Limited-BS4",
    "Chieftain-Elite-BS4",
    "Chieftain-Dark-Horse-BS4",
    "Indian-Chieftain-Classic-BS4",
    "Chieftain-BS4",
    "Chief-Vintage-BS4",
    "Chief-Dark-Horse-BS4",
    "Chief-Classic-BS4",
    "Chief",
    "Chief-Dark-Horse",
    "Chief",
]
Moto_Guzzi = ["California-1400-Touring", "Audace-1400"]
Aprilia = [
    "SXR-160",
    "SR-160",
    "SR-125",
    "Storm-125",
    "Tuono-BS4",
    "Facelift",
    "SRV-850",
    "RS4",
    "SR-150-Race",
    "SRV-850",
    "SR-150",
    "RSV4-(2012-2019)",
    "Caponord-1200",
    "Dorsoduro-1200",
    "Mana",
]
for i in companies:
    for j in eval(i):
        i = i.replace("rem", "")
        ur = (
            "https://www.zigwheels.com/user-reviews/"
            + str(i.replace("_", "-"))
            + "/"
            + str(j)
        )
        url.append(ur)
print(url)
print(len(url))