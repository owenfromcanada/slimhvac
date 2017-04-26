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
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('SlimHVAC', header_text)
        
        # He can see that there are no thermostats configured.
        table = self.browser.find_element_by_id('id_thermostat_table')
        self.assertTrue(len(table.find_elements_by_tag_name('tr')) == 0)
        
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
