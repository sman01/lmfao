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
url= "https://www.edmunds.com/car-reviews"
driver.get(url)
time.sleep(5)