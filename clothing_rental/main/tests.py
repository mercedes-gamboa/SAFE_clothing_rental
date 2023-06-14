from django.test import SimpleTestCase
from django.urls import reverse, resolve

from main.views import home_page


class TestUrlsMain(SimpleTestCase):
    def test_url_for_home(self):
        url = reverse('home')

        view = resolve(url).func
        self.assertEqual(view, home_page)
