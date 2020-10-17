
from django.contrib import admin
from django.urls import path
from lohae import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.buy, name="buy"),
]
