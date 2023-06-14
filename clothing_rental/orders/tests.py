from django.test import SimpleTestCase
from django.urls import reverse, resolve

from orders.views import OrderCreateView, OrderListView, OrderDeleteView, OrderDetailView, OrderStatusCreateView, \
    OrderStatusListView, OrderStatusDeleteView, OrderStatusDetailView, OrderStatusUpdateView, OrderLineCreateView, \
    OrderLineListView, OrderLineDeleteView, OrderLineDetailView, OrderLineUpdateView, OrderUpdateView


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

    def test_add_order_status_view_url(self):
        url = reverse('add_order_status')

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderStatusCreateView)

    def test_order_status_list_view_url(self):
        url = reverse('order_status_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderStatusListView)

    def test_delete_status_order_view_url(self):
        url = reverse('delete_status_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderStatusDeleteView)

    def test_detail_status_order_view_url(self):
        url = reverse('detail_status_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderStatusDetailView)

    def test_update_status_order_view_url(self):
        url = reverse('update_status_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderStatusUpdateView)

    def test_add_order_line_view_url(self):
        url = reverse('add_order_line')

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderLineCreateView)

    def test_order_line_list_view_url(self):
        url = reverse('order_line_list')

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderLineListView)


    def test_delete_line_order_view_url(self):
        url = reverse('delete_line_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderLineDeleteView)

    def test_detail_line_order_view_url(self):
        url = reverse('detail_line_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderLineDetailView)

    def test_update_line_order_view_url(self):
        url = reverse('update_line_order', args=[0])

        view = resolve(url).func.view_class
        self.assertEqual(view, OrderLineUpdateView)