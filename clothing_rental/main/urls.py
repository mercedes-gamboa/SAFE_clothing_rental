from django.urls import path
from main import views

urlpatterns = [
    path("home/", views.home_page, name='home'),
]