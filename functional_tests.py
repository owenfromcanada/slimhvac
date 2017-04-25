from selenium import webdriver
import unittest

class BasicViewTest(unittest.TestCase):  

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_check_current_temperature(self):
        # Adam wants to check the current temperature reading of the thermostat.
        # He navigates to the home page.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header shows the product name
        self.assertIn('SlimHVAC', self.browser.title)
        self.fail('Finish the test!')
        
        # He can see the current temperature displayed

if __name__ == '__main__':
    unittest.main()
