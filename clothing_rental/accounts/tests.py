from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import register, login_view, logout_view


class TestUrlsAccounts(SimpleTestCase):
    def test_url_for_registration(self):
        url = reverse('register')

        view = resolve(url).func
        self.assertEqual(view, register)

    def test_url_for_login(self):
        url = reverse('login')

        view = resolve(url).func
        self.assertEqual(view, login_view)

    def test_url_for_logout(self):
        url = reverse('logout')

        view = resolve(url).func
        self.assertEqual(view, logout_view)