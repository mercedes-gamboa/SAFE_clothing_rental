from django.test import SimpleTestCase
from django.urls import reverse, resolve

from about.views import about_page, ContactUs
class TestUrls(SimpleTestCase):

    def test_about_us_url(self):
        url = reverse('about')

        view = resolve(url).func
        self.assertEqual(view, about_page)

    def test_contact_us_url(self):
        url = reverse('contact_us')

        view = resolve(url).func.view_class
        self.assertEqual(view, ContactUs)