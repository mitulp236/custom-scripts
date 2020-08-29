from selenium import webdriver
from time import sleep
import sys
import os

try:
    gmail_email = str(sys.argv[1])
    gmail_password = str(sys.argv[2])
except IndexError:
    print("plase provide email and password as a argument")
    exit()

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(gmail_email)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()


sleep(5)

try:
    print(driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div').text)
    print("email is not valid")
    driver.quit()
    exit()
except Exception:
    print(" email is right ! ")

sleep(1)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(gmail_password)
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

sleep(2)

try:
    print(driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]').text)
    print("password wrong ! ")
    driver.quit()
    exit()
except Exception:
    print("password is right !")

print(" Loggedin successfully !")
driver.get("https://google.com")


# Run : python gmail_ckeck.py your_email your_password


