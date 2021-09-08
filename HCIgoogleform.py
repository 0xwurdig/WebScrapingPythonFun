from os import name
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys

# import ast
import concurrent.futures
import json
PATH = 'E:\chromedriver.exe'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
bad = []
# def getDrivers(n):
#     for  i in range(0,n):
#         i = webdriver.Chrome(PATH,options=chrome_options)
#         drivers.append(i)

def age(p):
    if(p<=3):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[1]/label').click()
    if(p<=45 and p>3):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[2]/label').click()
    if(p<=82 and p>45):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[3]/label').click()
    if(p>82):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[4]/label').click()
def gender(p):
    if(p<=53):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label').click()
    if(p<=80 and p>53):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label').click()
    if(p<=88 and p>80):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label').click()
    if(p>88):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[4]/label').click()
        
# def place(p):
#     ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


def occupation(p):
    if(p<=36):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label').click()
    if(p<=55 and p>36):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label').click()
    if(p<=57 and p>55):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label').click()
    if(p<=70 and p>57):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label').click()
    if(p<=76 and p>70):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]/label').click()
    if(p>76):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[6]/label').click()

def techsav(p):
    if(p<=17):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[1]').click()
    if(p<=26 and p>17):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[2]').click()
    if(p<=38 and p>26):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[3]').click()
    if(p<=90 and p>38):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[4]').click()
    if(p>90):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[5]').click()
def moodswings(p):
    if(p<=78):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[1]/label').click()
    if(p<=95 and p>78):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[2]/label').click()
    if(p>95):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[3]/label').click()


def helps(p):
    if(p<=72):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label').click()
    if(p<=60):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[2]/label').click()
    if(p<=65):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[3]/label').click()
    if(p<=17):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[4]/label').click()
    if(p<=41):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[5]/label').click()
def musichrs(p):
    if(p<=23):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[1]/label').click()
    if(p<=87 and p>23):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[2]/label').click()
    if(p<=96 and p>87):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[3]/label').click()
    if(p>96):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div/span/div/div[4]/label').click()
def project(p):
    if(p<=97):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[1]/label').click()
    if(p>97):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div/span/div/div[2]/label').click()

def diff(p):
    if(p<=84):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/label').click()
    if(p<=77):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[2]/label').click()
    if(p<=61):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[3]/label').click()
    if(p<=29):
        driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[4]/label').click()
    # if(p<=41):
    #     driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[5]/label').click()
# def comments():
driver = webdriver.Chrome(PATH,options=chrome_options)  
n = int(input())
for i in range(1,n+1):
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeIgYChWsIJiemk8e44KvNDSJ0UBp80Kh3czEeFGdT2_YrCkA/formResponse')
    p = float(i*100)/float(n)
    print(p)
    time.sleep(2)
    age(p)
    gender(p)
    occupation(p)
    techsav(p)
    moodswings(p)
    helps(p)
    musichrs(p)
    diff(p)
    project(p)
    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div').click()
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
