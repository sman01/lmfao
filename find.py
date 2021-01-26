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

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0"
}


driver = webdriver.Firefox()
models = []
years = []
page_count = 0
review = []
heading = []
sum = 0
rating = []
reviewer = []
date = []
dat = []
acktual = []
url = "https://www.zigwheels.com/user-reviews"
driver.get(url)
time.sleep(10)
for i in range(1, 70):

    revdat = driver.find_elements_by_xpath(
        "/html/body/main/div[3]/div[1]/div/span[2]/select/option[" + str(i) + "]"
    )
    for rev in revdat:
        rev.click()
        bec = rev.text.replace(" ", "-")
        if bec != "Select-Make":
            date.append(bec)
            print("cleek")
            b = bec.replace("-", "_")
            if b[0].isdigit():
                b = "rem" + b
            acktual.append(b)
            vars()[b] = []

            for j in range(1, 70):
                revdate = driver.find_elements_by_xpath(
                    "/html/body/main/div[3]/div[1]/div/span[3]/select/option["
                    + str(j)
                    + "]"
                )
                for re in revdate:
                    be = re.text.replace(" ", "-")
                    if be != "Select-Model":
                        vars()[b].append(be)
        else:
            continue


driver.quit()
print("Done")
print(acktual)
for car in acktual:
    print(f"{car} = {eval(car)}")
print("Allover")