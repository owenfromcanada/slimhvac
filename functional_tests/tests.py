from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

class BasicViewTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > 10:
                    raise e
                time.sleep(0.1)

    def test_check_current_temperature(self):
        # Adam wants to check the current temperature reading of the thermostat.
        # He navigates to the home page.
        self.browser.get(self.live_server_url)

        # He notices the page title and header shows the product name
        self.assertIn('SlimHVAC', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('SlimHVAC', header_text)
        
        # He can see that there are no thermostats configured.
        table = self.browser.find_element_by_id('id_thermostat_table')
        self.assertTrue(len(table.find_elements_by_tag_name('tr')) == 0)
    
    def test_check_add_thermostat(self):
        # Adam notices a link to add a new thermostat on the start page.
        self.browser.get(self.live_server_url)
        button = self.browser.find_element_by_id('id_new_thermostat_button')
        button.click()
        
        # He waits for the page to load
        self.wait_for(lambda: self.assertEqual(self.browser.current_url, self.live_server_url + '/thermostat/new'))
        
        # He notices the page header indicates he's adding a new thermostat.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('New Thermostat', header_text)
        
        # He sees various input fields.
        name_input = self.browser.find_element_by_id('id_name')
        zwave_id_input = self.browser.find_element_by_id('id_zwave_id')
        
        # He types in a name and id for the thermostat.
        name_input.send_keys('Main Thermostat')
        zwave_id_input.send_keys('1')
        
        # He clicks the submit button.
        submit_button = self.browser.find_element_by_id('id_submit')
        submit_button.click()
        
        # He is redirected to the start page
        self.wait_for(lambda: self.assertEqual(self.browser.current_url, self.live_server_url + '/'))
        
        # Where his new thermostat is displayed
        table = self.browser.find_element_by_id('id_thermostat_table')
        self.assertTrue(len(table.find_elements_by_tag_name('tr')) == 1)
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Main Thermostat', [row.text for row in rows])
