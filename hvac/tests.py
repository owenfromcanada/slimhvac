from django.core.urlresolvers import resolve
from django.test import TestCase

from hvac.models import Thermostat
from hvac.views import start_page

class StartPageTest(TestCase):

    def test_root_url_resolves_to_start_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, start_page)

    def test_start_page_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'start.html')
    
    def test_start_page_redirects_after_post_request(self):
        response = self.client.post('/', data={'name_text': 'Thermostat name', 'zwave_id_text': '1'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
    
    def test_new_thermostat_saved(self):
        self.assertEqual(Thermostat.objects.count(), 0)
        self.client.post('/', data={'name_text': 'Thermostat name', 'zwave_id_text': '1'})
        self.assertEqual(Thermostat.objects.count(), 1)
        self.assertEqual(Thermostat.objects.first().name, 'Thermostat name')
    
    def test_displays_all_thermostats(self):
        Thermostat.objects.create(name='First thermostat', zwave_id='1')
        Thermostat.objects.create(name='Second thermostat', zwave_id='2')
        
        response = self.client.get('/')
        
        self.assertIn('First thermostat', response.content.decode())
        self.assertIn('Second thermostat', response.content.decode())


class ThermostatPageTest(TestCase):

    def test_new_thermostat_template_used(self):
        response = self.client.get('/thermostat/new')
        self.assertTemplateUsed(response, 'new.html')


class ThermostatModelTest(TestCase):
    
    def test_saving_and_retrieving_thermostats(self):
        first_therm = Thermostat()
        first_therm.name = 'Name of first'
        first_therm.zwave_id = 1
        first_therm.save()
        
        second_therm = Thermostat()
        second_therm.name = 'Second thermostat'
        second_therm.zwave_id = 2
        second_therm.save()
        
        saved_therms = Thermostat.objects.all()
        self.assertEqual(saved_therms.count(), 2)
        self.assertEqual(saved_therms[0].name, 'Name of first')
        self.assertEqual(saved_therms[1].name, 'Second thermostat')
        