from selenium import webdriver
import time
from urllib.request import Request, urlopen
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import pandas as pd
import csv
from itertools import zip_longest
from selenium.common.exceptions import MoveTargetOutOfBoundsException
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0'}





review=[]
purpos=[]
subdire=[]
supersu=[]
ratings=[]
dates=[]
users=[]




driver = webdriver.Firefox()
driver.set_window_size(640,720)
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
    id='//div[@id="userReviews"]/div['+str(j)+']/div/div[2]/div/p/span[2]'
    try:
        btn= driver.find_element_by_xpath(id)
        btn.click()
        res+=1
    except:
        continue
print('done expanding')
for i in range(1,20):
    
    '''
    //*[@id="userReviews"]
    /html/body/div[15]/div/div[1]/section/div[3]/div[3]
    /html/body/div[15]/div/div[1]/section/div[3]/div[3]/div[12]/div/div[2]/div/p
    //*[@id="overflow_hidden_2183655"]/div/div[2]/div/p
    '''
    time.sleep(1)
    review_id = '//div[@id="userReviews"]/div['+str(i)+']/div/div[2]/div/p' 
    try:
        purpose='//div[@id="userReviews"]/div['+str(i)+']/div/div[2]/div/p/span[3]'
    except:
        purpose='//div[@id="userReviews"]/div['+str(i)+']/div[11]/div/div[2]/div/p/span[3]'
    
    subdir='//div[@id="userReviews"]/div['+str(i)+']/div/div[2]/div/p/span[3]/span'
    supersub='//div[@id="userReviews"]/div['+str(i)+']/div/div[2]/div/p/span[3]/span[2]'
    rating_path='//div[@id="userReviews"]/div['+str(i)+']/div/div[1]/div[1]/span[2]/span' ####rating\
    date_path='//div[@id="userReviews"]/div['+str(i)+']/div/div[1]/div[1]/span[3]' ####date
    user_path='//div[@id="userReviews"]/div['+str(i)+']/div/div[1]/div[1]/span[1]/span'###customer    
    try:
        review=driver.find_elements_by_xpath(review_id)
        purpos=driver.find_elements_by_xpath(purpose)
        print(purpos)
        try:
            subdire=driver.find_element_by_xpath(subdir)
        except:
            e0='subdire not found'
        try:
            ratings=driver.find_elements_by_xpath(rating_path)
            dates=driver.find_elements_by_xpath(date_path)
            users=driver.find_elements_by_xpath(user_path)
        except:
            e4='ratings, dates, users not found'
        try:
            supersu=driver.find_element_by_xpath(supersub)
        except:
            e1='supersu not found'
        print(f'----------------------------------------  Review number :: {i}  ----------------------------------------')
        for (purp, rev, rat,dat,use) in zip(purpos,review,ratings,dates,users):
            revew=rev.text.replace(purp.text,'')
            try:
                lmao=purp.text.replace(subdire.text,'')
                subtract=lmao.replace(supersu.text,'')
            except:
                e2='subtact and lmao not found'
            '''
            print(f'Date: {dat.text}')
            print(f'Rating: {rat.text}')
            print(f'Review: {revew}')
            print(f'Customer: {use.text}')
            print(f'Used for: {subtract}') ### what the car is used for i.e daily commute/ family car , etc.
            '''

    except:
        print("AD")
        continue
print("alldoen")
driver.quit()