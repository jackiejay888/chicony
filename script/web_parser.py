#!/usr/bin/python
'''
Created on 2023/08/22

@author: ZL Chen
@title: Web parser
'''

import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from HTMLTestRunner.runner import HTMLTestRunner

class web_paresr(unittest.TestCase):
	def setUp(self):
		options = webdriver.ChromeOptions()
		options.add_argument('--incognito')
		options.add_argument('ignore-certificate-errors')
		service = webdriver.ChromeService('chromedriver.exe')
		self.driver = webdriver.Chrome(service=service, options=options)

	def test_01_google(self):
		self.driver.get('https://www.google.com.tw/')
		try:
			element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.ID, 'APjFqb'))
			)
			element.send_keys('chicony')
			element.send_keys(Keys.ENTER)
			print('Passed')
		except:
			print('Failed')
		finally:
			self.driver.quit

	def test_02_chicony(self):	
		self.driver.get('https://iwa.chiconypower.com/')
		try:
			WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.ID, 'logo'))
			)
			print('Passed')
		except:
			print('Failed')
		finally:
			self.driver.quit

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	suite = unittest.TestSuite(unittest.TestLoader().loadTestsFromTestCase(web_paresr))
	runner = HTMLTestRunner(
		log=True, verbosity=2, output='report', title='Test report', report_name='report', 
		open_in_browser=True, description='HTMLTestReport', tested_by='ZL', add_traceback=False
	)
	runner.run(suite)