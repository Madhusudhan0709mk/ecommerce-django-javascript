
import razorpay
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Avg,Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from django.core.cache import cache
CACHE_TTL = getattr(settings,'CACHE_TTL',60*15)
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})


def category_product_list(request,cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(category=category)
    context = {
        'category':category,
        'products':products
    }
    return render(request,'category/category_product_list.html',context)


def product_detail_view(request, pid):
    if cache.get(pid):
        product = cache.get(pid)
        print("data from cache")
    else:    
        product = get_object_or_404(Product, pid=pid)
        try:
            cache.set(pid,product)
            print("DATA FROM DB")
            productreview = ProductReview.objects.get(product=product)
            starrating = "★" * productreview.rating + "☆" * (5 - productreview.rating)
            reviewcount = ProductReview.objects.filter(product=product).count()
            avg_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))
        
        except ProductReview.DoesNotExist:
            productreview = None
            starrating = None
            reviewcount = 0
            avg_rating = {'rating__avg': None} 
            
    if 'productreview' not in locals():
        productreview = None
        starrating = None
        reviewcount = 0
        avg_rating = {'rating__avg': None}
   

    context = {
        'product':product,
        'productreview':productreview,
        'starrating':starrating,
        'reviewcount':reviewcount,
        'avg_rating':avg_rating,
        
        
    }
    return render(request, 'products/product_detail_view.html',context)

def addtocart(request,pid):
    product = get_object_or_404(Product,pid=pid)
    user = request.user
    
    cart_item,created = CartOrderItems.objects.get_or_create(
        product=product,
        user=user
        )
    if created:
        # If the item is newly created, set its quantity to 1
        cart_item.quantity = 1
        cart_item.save()
    else:
        # If the item already exists in the cart, increment its quantity by 1
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request,"Product added successfully")
    cart_items= CartOrderItems.objects.filter(user=user)
    sum = 0
    for item in cart_items:
        item.total = item.price * item.quantity
        
        sum += item.total
        item.save()
        
        
    
    context = {
        'cart_items':cart_items,
        'user':user,
        'sum': sum  
    }
    return render(request,'carts/cart.html',context)

@login_required
def viewaddtocart(request):
    user= request.user
    viewaddtocart = CartOrderItems.objects.filter(user=user)
    sum = 0
    for item in viewaddtocart:
        item.total = item.price * item.quantity
        sum += item.total
        item.save()
        
    context={
        'viewaddtocart':viewaddtocart,
        'sum': sum  
    }
    return render(request,'carts/viewaddtocart.html',context)

@login_required
def searchindex(request):
    if request.method == 'POST':
        searched = request.POST.get('searched','')  # Use get() method instead of dictionary-like key access
        results = Product.objects.filter(Q(title__icontains=searched))
        if results:
            messages.success(request, 'Your search results')
        else:
            messages.info(request, 'No results found')
        return render(request, 'results.html', {'results': results})
    return render(request, 'index.html')

@login_required 
def shopdetail(request):
    return render(request,'shopdetail.html')



razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))

def checkout(request):
    
    user = request.user
    cartitems = CartOrderItems.objects.filter(user=user)
    sum = 0

    for item in cartitems:
        item.total = item.price * item.quantity
        sum += item.total
        item.save()
        
    context={
        'cartitems':cartitems,
        'sum':sum,
    
    }  
    return render(request, 'checkout.html', context)


def place_order(request):
    user = request.user
    cartitems = CartOrderItems.objects.filter(user=user)
    sum = 0

    for item in cartitems:
        item.total = item.price * item.quantity
        sum += item.total
        item.save()
        
    # razorpay order creating
    order_amount  = int(sum * 100)
    order_currency = 'INR'
    order_receipt = f'order_rcptid_{user.id}'
    
    razorpay_order = razorpay_client.order.create({
        'amount':order_amount ,
        'currency':order_currency,
        'receipt':order_receipt
    })
    
    cart_order = CartOrder.objects.create(
        user= user,
        price= sum,
        razorpay_order_id = razorpay_order['id']
    )
    
    cart_order.order.set(cartitems)
    
    context={
        'cartitems':cartitems,
        'sum':sum,
        'razorpay_order_id': razorpay_order['id'],
        'razorpay_key': settings.RAZORPAY_KEY_ID,
        'currency': order_currency,
        'callback_url': 'payment_handler/'
    }  
    return render(request, 'checkout.html', context)
    

#  making payment handler vie taken from the checkout script form action of razorpay
@csrf_exempt
def payment_handler(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id','')
        order_id = request.POST.get('razorpay_order_id','')
        signature = request.POST.get('razorpay_signature', '')
        
        order = CartOrder.objects.get(razorpay_order_id = order_id)
        
        try:
            order.paid = True
            order.razorpay_payment_id = payment_id
            order.razorpay_payment_status = 'success'
            order.razorpay_signature=signature
            order.save()
            messages.success(request,'order confirmed ')
            return redirect('home')
        
        except:
            order.razorpay_payment_status = 'failed'
            order.save()
            messages.success(request,'order failed ')
            return redirect('home')
        
    return HttpResponseBadRequest()


def my_orders(request):
    user = request.user
    paid_orders = CartOrder.objects.filter(user=user, paid=True).prefetch_related('order')

    context = {
        'paid_orders': paid_orders,
    }
    return render(request, 'order/my_orders.html', context)

# invoice for billing:
def invoice(request):
    return render(request,'invoice/invoice.html')


@login_required 
def shop(request):
    return render(request,'shop.html')


@login_required
def vendorsview(request):
    vendors = Vendor.objects.all()
    return render(request,'vendor/vendorsview.html',{'vendors':vendors})