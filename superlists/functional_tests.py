from selenium import webdriver
import unittest

# Option 1 - with ChromeOptions
class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		self.browser = webdriver.Chrome(chrome_options=chrome_options)
		self.browser.implicitly_wait(3)
	def tearDown(self):
		print('쌤말아')
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://192.168.0.2:8080')
		print('ggg' + self.browser.title)
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the Test!')
if __name__ == '__main__':
	unittest.main(warnings='ignore')



