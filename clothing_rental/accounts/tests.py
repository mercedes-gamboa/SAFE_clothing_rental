from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import register, update_profile, login_view, logout_view

class TestUrlsAccounts(SimpleTestCase):
    def test_url_for_registration(self):
        url = reverse('register')

        view = resolve(url).func
        self.assertEqual(view, register)

    def test_url_for_profile(self):
        url = reverse('profile')

        view = resolve(url).func
        self.assertEqual(view, update_profile)

    def test_url_for_login(self):
        url = reverse('login')

        view = resolve(url).func
        self.assertEqual(view, login_view)

    def test_url_for_logout(self):
        url = reverse('logout')

        view = resolve(url).func
        self.assertEqual(view, logout_view)