from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('prodcut/<int:product_id>', product_detail, name="prodcut_detail"),
]
