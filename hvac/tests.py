from django.core.urlresolvers import resolve
from django.test import TestCase

from hvac.views import start_page  

class StartPageTest(TestCase):

    def test_root_url_resolves_to_start_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, start_page)

    def test_start_page_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'start.html')


class ThermostatPageTest(TestCase):

    def test_new_thermostat_template_used(self):
        response = self.client.get('/thermostat/new')
        self.assertTemplateUsed(response, 'new.html')

