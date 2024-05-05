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
    path('increment_quantity/<str:pid>/',views.increment_quantity,name='increment_quantity'),
    path('addtocart/<str:pid>/',views.addtocart,name='addtocart'),
    path('vendorsview/',views.vendorsview,name='vendorsview'),
     path('viewaddtocart/',views.viewaddtocart,name='viewaddtocart'),
    
]
