from django.urls import path
from orders import views

urlpatterns = [
    path("add/order/", views.OrderCreateView.as_view(), name="add_order"),
    path("list/order/", views.OrderListView.as_view(), name="order_list"),
    path("delete/order/<int:pk>/", views.OrderDeleteView.as_view(), name="delete_order"),
    path("detail/order/<int:pk>/", views.OrderDetailView.as_view(), name="detail_order"),
    path("update/order/<int:pk>/", views.OrderUpdateView.as_view(), name="update_order"),

]