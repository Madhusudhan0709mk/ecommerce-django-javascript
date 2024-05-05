from django.contrib import admin
from .models import *
# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']

# class CartOrderAdmin(admin.ModelAdmin):
#     list_display=['user','price','paid_status','product_status','order_date']
    
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display=['quantity','price','total']


class AddressAdmin(admin.ModelAdmin):
    list_display=['user','address','status']
    
class WishlistAdmin(admin.ModelAdmin):
    list_display=['user','product','date']
    
class ProductAdmin(admin.ModelAdmin):
    list_display=['vendor','category','title','price','old_price','product_status','in_stock','status','digital','featured','date']

class VendorAdmin(admin.ModelAdmin):
    list_display=['user','title','address','contact']
    
class ProductReviewAdmin(admin.ModelAdmin):
    list_display=['user','product','review','rating','date']  
    
class ProductImagesAdmin(admin.ModelAdmin):
    list_display=['product','date']  
    
admin.site.register(Category,CategoryAdmin)
# admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImages,ProductImagesAdmin)
admin.site.register(ProductReview,ProductReviewAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(Tags)