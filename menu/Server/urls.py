from django.urls import path
# now import the views.py file into this code
from . import views

urlpatterns = [
    path("get/", views.get_menu),
    path("connect/",views.connect_to_mysql)
]
