from django.urls import path
from . import views
# now import the views.py file into this code
urlpatterns = [
    path("get/", views.get_menu),
    path("connect/",views.connect_to_mysql),
    path('get/get_menu', views.result, name='result'),
]
