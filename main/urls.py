from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('shopdetail/',views.shopdetail,name='shopdetail'),
    path('searchindex/',views.searchindex,name='searchindex'),
    
    path('checkout/',views.checkout,name='checkout'),
    
    path('shop/',views.shop,name='shop'),
    path('categories/', views.category_list, name='category_list'),
    path('category_product_list/<str:cid>/',views.category_product_list,name='category_product_list'),
    path('product_detail_view/<str:pid>/',views.product_detail_view,name='product_detail_view'),
    path('addtocart/<str:pid>/',views.addtocart,name='addtocart'),
    path('vendorsview/',views.vendorsview,name='vendorsview'),
    path('viewaddtocart/',views.viewaddtocart,name='viewaddtocart'),
    
    path('payment_handler/',views.payment_handler, name='payment_handler'),
    path('my-orders/',views.my_orders, name='my_orders'),
    
    path('order_success/',views.payment_handler, name='order_success'),
    path('order_failure/', views.payment_handler, name='order_failure'),
     path('place-order/',views.place_order, name='place_order'),
     
     path('invoice/',views.invoice,name='invoice')

]
