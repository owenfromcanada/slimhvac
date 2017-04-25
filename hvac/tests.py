from django.core.urlresolvers import resolve
from django.test import TestCase
from hvac.views import start_page  

class MainPageTest(TestCase):

    def test_root_url_resolves_to_start_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, start_page)  
