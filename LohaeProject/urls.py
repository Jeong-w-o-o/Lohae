from django.contrib import admin
from django.urls import path, include
from lohae import views
from django.contrib.auth.views import LoginView, LogoutView
from lohae.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', views.main, name="main"),
    path('main', views.main, name="main"),
    path('productlist', views.productlist, name="productlist"),
    path('buy_item/', views.buy_item, name="buy_item"),
    path('write_messages/', views.write_messages, name="write_messages"),
    path('signup/', views.signup, name="signup"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('mypage/', views.mypage, name="mypage"),
    path('change/', views.change, name="change"),
    path('changepass/', views.user_change_pass, name="changepass"),
    path('buy_item2/', views.buy_item2, name="buy_item2"),
    path('buy_item3/', views.buy_item3, name="buy_item3"),
]

