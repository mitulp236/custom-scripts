from selenium import webdriver
from time import sleep
import sys
import os

try:
    repository_name = str(sys.argv[1])
except IndexError:
    print("plase provide repository name as a argument")
    exit()

github_username = "Enter Your Github Username"
github_password = "Enter Your Github Password"

driver = webdriver.Chrome("C:\\chromedriver.exe")
driver.get("https://github.com/login")
driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(github_username)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(github_password)
driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()

try:
    print(driver.find_element_by_xpath('//*[@id="js-flash-container"]/div/div').text)
    print("try again with correct username and password !")
    print("Thank you__________!")
    driver.quit()
    exit()
except:
    pass
driver.get("https://github.com/new")
driver.find_element_by_xpath('//*[@id="repository_name"]').send_keys(repository_name)

sleep(1)

if driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd[2]').get_attribute("class") == 'error':
    print('this repo is already exist ! try again with unique repo name')
    print("Thank you__________!")
    driver.quit()
    exit()

# if you want to make your repo private then uncomment below line
# driver.find_element_by_xpath('//*[@id="repository_visibility_private"]').click()

# if you don't want to initialize your repo with README.MD then comment below line
driver.find_element_by_xpath('//*[@id="repository_auto_init"]').click()

driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button').click()

# https://github.com/rockstart07/dwlijflw.git // clone this

executable_command = '"cd /d d:\myProjects\ & git clone https://github.com/{0}/{1}.git & cd {2} & code . & exit"'.format(github_username,repository_name, repository_name)
os.system('cmd /k {0}'.format(executable_command))

print("project created successfully !")
print("___________________Thank You____________________________________")
driver.quit()

