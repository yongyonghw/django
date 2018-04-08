from selenium import webdriver
import unittest

# Option 1 - with ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('http://192.168.0.2:8080')

assert 'Django' in driver.title
