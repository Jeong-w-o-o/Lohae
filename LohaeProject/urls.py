
from django.contrib import admin
from django.urls import path
from lohae import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('productlist', views.productlist, name="productlist"),
    path('buy_item/', views.buy_item, name="buy_item"),
    path('write_messages/', views.write_messages, name="write_messages"),


]
