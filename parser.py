from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(1)
driver.get('https://www.google.com.tw/')
sleep(1)

driver.close()

