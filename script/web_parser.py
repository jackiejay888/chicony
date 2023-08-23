#!/usr/bin/python
'''
Created on 2023/08/22

@author: ZL Chen
@title: Web parser
'''

from selenium import webdriver

driver = webdriver.Chrome()
# driver.get('https://iwa.chiconypower.com/')
driver.get('https://www.google.com.tw/')
driver.close()

