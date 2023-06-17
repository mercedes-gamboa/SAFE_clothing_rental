from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from orders.models import Order
from orders.forms import OrderForm


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

