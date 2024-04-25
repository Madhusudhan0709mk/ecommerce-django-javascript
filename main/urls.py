from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('shopdetail/',views.shopdetail,name='shopdetail'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('shop/',views.shop,name='shop')
]
