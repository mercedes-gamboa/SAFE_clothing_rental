from django.test import SimpleTestCase
from django.urls import reverse, resolve

from orders.views import OrderCreateView, OrderListView, OrderDeleteView, OrderDetailView,  OrderUpdateView


class TestUrlsOrders(SimpleTestCase):
    def test_add_order_view_url(self):
        url = reverse('add_order')

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderCreateView)

    def test_order_list_view_url(self):
        url = reverse('order_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderListView)

    def test_delete_order_view_url(self):
        url = reverse('delete_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderDeleteView)

    def test_detail_order_view_url(self):
        url = reverse('detail_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderDetailView)

    def test_update_order_view_url(self):
        url = reverse('update_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderUpdateView)

