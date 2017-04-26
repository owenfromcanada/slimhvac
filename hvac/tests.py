from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from hvac.views import start_page  

class MainPageTest(TestCase):

    def test_root_url_resolves_to_start_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, start_page)  

    def test_start_page_returns_correct_html(self):
        request = HttpRequest()
        response = start_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>SlimHVAC</title>', html)
        self.assertTrue(html.endswith('</html>'))
