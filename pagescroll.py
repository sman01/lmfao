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





review=[]
purpos=[]
subdire=[]
supersu=[]
ratings=[]
dates=[]
users=[]




driver = webdriver.Firefox()
driver.set_window_size(360,480)
url= "https://www.zigwheels.com/user-reviews/Maruti-Suzuki/Swift"
driver.get(url)
time.sleep(5)
f=0
ID='//*[@id="loadMore"]/span'

revs='/html/body/div[15]/div/div[1]/section/div[2]/div[1]/div/div/span'
reviews =  driver.find_element_by_xpath(revs)
review=reviews.text.replace('reviews','')
reviewno=int(review)
print(f'Number of reviews for this car {reviewno}')
res=0
while True:
    try:
    # finding the button using ID
        button =  driver.find_element_by_xpath(ID)

# clicking on the button
        button.click()
        f+=1
        time.sleep(0.5)
    except:
        break
print("Thats all folks")
print (f)
for j in range (1,reviewno):
    id='/html/body/div[15]/div/div[1]/section/div[3]/div[3]/div['+str(j)+']/div/div[2]/div/p/span[2]'
    try:
        btn= driver.find_element_by_xpath(id)
        btn.click()
        res+=1
    except:
        continue
print('done expanding')
for i in range(1,5):
    time.sleep(1)
    review_id = '/html/body/div[15]/div/div[1]/section/div[3]/div[3]/div['+str(i)+']/div/div[2]/div/p' 
    purpose='/html/body/div[15]/div/div[1]/section/div[3]/div[3]/div['+str(i)+']/div/div[2]/div/p/span[3]'
    subdir='/html/body/div[15]/div/div[1]/section/div[3]/div[3]/div['+str(i)+']/div/div[2]/div/p/span[3]/span'
    supersub='/html/body/div[15]/div/div[1]/section/div[3]/div[3]/div['+str(i)+']/div/div[2]/div/p/span[3]/span[2]'
    rating_path='/html/body/div[15]/div/div[1]/section/div[3]/div[3]/div['+str(i)+']/div/div[1]/div[1]/span[2]/span' ####rating\
    date_path='/html/body/div[15]/div/div[1]/section/div[3]/div[3]/div['+str(i)+']/div/div[1]/div[1]/span[3]' ####date
    user_path='/html/body/div[15]/div/div[1]/section/div[3]/div[3]/div['+str(i)+']/div/div[1]/div[1]/span[1]/span'###customer    
    try:
        review=driver.find_elements_by_xpath(review_id)
        purpos=driver.find_elements_by_xpath(purpose)
        subdire=driver.find_elements_by_xpath(subdir)
        supersu=driver.find_elements_by_xpath(supersub)
        ratings=driver.find_elements_by_xpath(rating_path)
        dates=driver.find_elements_by_xpath(date_path)
        users=driver.find_elements_by_xpath(user_path)
        print(f'----------------------------------------  Review number :: {i}  ----------------------------------------')
        for (purp,sub,supers,rev,rat,dat,use) in zip(purpos,subdire,supersu,review,ratings,dates,users):
            if purpos == None:
                print('ayyyyy')
                ### Customer review
            else:
                revew=rev.text.replace(purp.text,'')
                print(purpos)
            if supersu!=[]:
                lmao=purp.text.replace(supers.text,'')
            if subdire!=[]:
                subtract=lmao.replace(sub.text,'')
                '''
            print(f'Date: {dat.text}')
            print(f'Rating: {rat.text}')
            print(f'Review: {revew}')
            print(f'Customer: {use.text}')
            print(f'Used for: {subtract}') ### what the car is used for i.e daily commute/ family car , etc.
            '''


    except:
        print("exception")
        continue
print("alldoen")
driver.quit()
