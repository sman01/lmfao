from selenium import webdriver
import time
from urllib.request import Request, urlopen
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import pandas as pd
import csv
from itertools import zip_longest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'}


driver = webdriver.Firefox()
models=[]
years=[]
page_count=0
review=[]
heading=[]
sum=0
rating=[]
reviewer=[]
date=[]
url= "https://www.zigwheels.com/user-reviews/Maruti-Suzuki/800"
driver.get(url)
time.sleep(5)
f=0
ID='//*[@id="loadMore"]/span'
while True:
    try:
    # finding the button using ID
        button =  driver.find_element_by_xpath(ID)

# clicking on the button
        button.click()
        f+=1
        time.sleep(5)
    except:
        break
print("Thats all folks")
print (f)
driver.quit()