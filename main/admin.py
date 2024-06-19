from django.contrib import admin
from .models import *
# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']

class CartOrderAdmin(admin.ModelAdmin):
    list_display=['user','price','product_status','order_date']
    
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display=['quantity','price','total']
   
class ProductAdmin(admin.ModelAdmin):
    list_display=['vendor','category','title','price','old_price','in_stock','status','digital','featured','date']

class VendorAdmin(admin.ModelAdmin):
    list_display=['user','title','address','contact']
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Tags)