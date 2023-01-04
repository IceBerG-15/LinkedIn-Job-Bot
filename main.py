from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv('projects\Automating jobs on LinkedIn\.env')

chrome_driver_path="C:\\Python310\\chrome_driver\\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3424115353&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom')

sign_in=driver.find_element('xpath','/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

user_email=driver.find_element('xpath','//*[@id="username"]')
user_email.send_keys(os.getenv('EMAIL'))

password=driver.find_element('xpath','//*[@id="password"]')
password.send_keys(os.getenv('PASS'))
password.send_keys(Keys.ENTER)

save=driver.find_element('xpath','//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
save.click()

follow=driver.find_element('xpath','//*[@id="ember300"]/section/div[1]/div[1]/button/span')
follow.click()


time.sleep(60)
driver.quit()
