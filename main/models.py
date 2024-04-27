from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.conf import settings

STATUS_CHOICE={
    ("process","Processing"),
    ("shipped","Shipped"),
    ("delivered","Delivered"),
}

STATUS={
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("rejected","Rejected"),
    ("in_review","In_review"),
    ("rejected","Rejected"),
}

RATING = {
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★"),
}


class Category(models.Model):
    # cid = models.UUIDField(unique=True)
    cid = ShortUUIDField(unique=True,length = 10,max_length=30,prefix='cat',alphabet="adcdefgh12345")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/images/',null=True,blank=True)
    
    
    def __str__(self):
        return self.title
    
class Vendor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    
    vid = ShortUUIDField(unique=True,length = 10,max_length=30,prefix='ven',alphabet="adcdefgh12345")
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    contact = models.CharField(max_length=100,default="165-demo-695")
    image = models.ImageField(upload_to='vendor/images/',null=True,blank=True)
    chat_resp_time = models.CharField(max_length=100,default="100")
    shipping_on_time = models.CharField(max_length=100,default="100")
    authentic_rating = models.CharField(max_length=100,default="100")
    days_return = models.CharField(max_length=100,default="100")
    warranty_period = models.CharField(max_length=100,default="100")
    
    
    def __str__(self):
        return self.title
    

class Tags(models.Model):
    pass
    
class Product(models.Model):
    
    pid = ShortUUIDField(unique=True,length=10,max_length=20,alphabet="abcdefgh12345",prefix="pro")
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    
    
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product/images/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    
    price = models.DecimalField(max_digits=999999999,decimal_places=2,default="100")
    old_price = models.DecimalField(max_digits=999999999,decimal_places=2,default="100")
    
    specifications = models.TextField(null=True,blank=True)
    tags = models.ForeignKey(Tags,on_delete=models.SET_NULL,null=True)
    
    product_status = models.CharField(choices=STATUS,max_length=10,default="in_review")
    in_stock = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    digital = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    sku = ShortUUIDField(unique=True,length=4,max_length=20,alphabet="1234567890",prefix="sku")
    
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True,blank=True)
    
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price/self.old_price)*100
        return new_price
    
    
class ProductImages(models.Model):
    image= models.ImageField(upload_to="product/images/",null=True,blank=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null =True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural="Product Images"
    
class CartOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=100)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE,max_length=10,default="processing")
    
    
    # class Meta:
    #     verbose_name_plural="Cart Order"
    
    
class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)  
    image= models.ImageField(upload_to="cartorderitems/images/",null=True,blank=True)
    quantity = models.IntegerField(default = 0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default="100")
    total = models.DecimalField(max_digits=12,decimal_places=2,default="100")
    
    class Meta:
        verbose_name_plural="Cart Order Items"
        
    def order_img(self):
        return self.image
    
class ProductReview(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null =True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING,default=None)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural="Product Review"
        
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    
class  Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null =True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural="Wishlist"
        
    def __str__(self):
        return self.product.title
    
class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length=225,null =True)
    status = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural="Address"