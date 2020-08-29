from selenium import webdriver
from time import sleep
import sys
import os

try:
    email = str(sys.argv[1])
    password = str(sys.argv[2])
except IndexError:
    print("plase provide email and password as a argument")
    exit()

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.implicitly_wait(100)

driver.get("https://www.awseducate.com/student/s/awssite")

# login page
driver.find_element_by_xpath('//*[@id="loginPage:siteLogin:loginComponent:loginForm:username"]').send_keys(email)
driver.find_element_by_xpath('//*[@id="loginPage:siteLogin:loginComponent:loginForm:password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginBlock"]/div/div/div[2]/div/p/a').click()

# second page
new_page = driver.find_element_by_xpath('//*[@id="ltiLaunchForm"]/div/div/div[2]/a').get_attribute('href')

driver.get(new_page)
# final page
driver.find_element_by_xpath('//*[@id="awsbtn"]').click()




