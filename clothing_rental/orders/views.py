from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy

from accounts.models import ShoppingCart
from orders.models import Order, OrderLine, OrderStatus
from orders.forms import OrderForm, OrderLineForm, OrderStatusForm


from products.models import ClothingItem

# Create your views here.

"""Order Views"""
class OrderListView(LoginRequiredMixin,View):
    def get_login_url(self, request):
        order = Order.objects.get(user=request.user)
        context = {"order": order}
        return render(request, "orders/order_list.html", context)

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("order_list")
    template_name = "orders/add_order.html"

# class NewOrderView(LoginRequiredMixin, View):
#     def get(self, request):
#         cart_items = ShoppingCart.objects.filter(user=request.user)
#         order = Order.objects.create(user=request.user)
#
#         for cart_item in cart_items:
#             order.create()

    # def get(self, request):
    #     user =
    #     shopping_cart = ShoppingCart.objects.get(user=request.user)
    #
    # def get_queryset(self):
    #     query = ShoppingCart.ClothingItem.objects.all()[:1]
    #     return query



class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy("order_list.html")
    template_name = "orders/delete_order.html"

class OrderDetailView(DeleteView):
    model = Order
    template_name = "orders/detail_order.html"

class OrderUpdateView(UpdateView):
    model = Order
    template_name = "orders/update_order.html"
    form_class = OrderForm

