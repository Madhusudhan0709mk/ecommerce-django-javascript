from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Avg,Q
from django.core.exceptions import ObjectDoesNotExist

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
    product = get_object_or_404(Product, pid=pid)
    try:
        productreview = ProductReview.objects.get(product=product)
        starrating = "★" * productreview.rating + "☆" * (5 - productreview.rating)
        reviewcount = ProductReview.objects.filter(product=product).count()
        avg_rating = ProductReview.objects.filter(product=product).aggregate(Avg('rating'))
        
    except:
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


def increment_quantity(request, pid):
    if request.method == 'POST':
       
        product = Product.objects.get(pid=pid)
        
        
        product.quantity += 1
        product.save()
        
        
        # messages.success(request, 'Quantity incremented successfully!')
        
        
        return redirect('product_detail_view', pid=pid)
    
    

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
    else:
        # If the item already exists in the cart, increment its quantity by 1
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request,"Product added successfully")
    cart_items= CartOrderItems.objects.filter(user=user)
    sum = 0
    for item in cart_items:
        item.total_price = item.price * item.quantity
        
        sum += item.total_price
        
        
    
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
        item.total_price = item.price * item.quantity
        
        sum += item.total_price
    context={
        'viewaddtocart':viewaddtocart,
        'sum': sum  
    }
    return render(request,'carts/viewaddtocart.html',context)

@login_required
def searchindex(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')  # Use get() method instead of dictionary-like key access
        results = Product.objects.filter(title__icontains=searched)
        if results:
            messages.success(request, 'Your search results')
        else:
            messages.info(request, 'No results found')
        return render(request, 'results.html', {'results': results})
    return render(request, 'index.html')

@login_required 
def shopdetail(request):
    return render(request,'shopdetail.html')

# @login_required 
# def cart(request):
#     return render(request,'carts/cart.html')

@login_required 
def checkout(request):
    return render(request,'checkout.html')


@login_required 
def shop(request):
    return render(request,'shop.html')

@login_required
def vendorsview(request):
    vendors = Vendor.objects.all()
    return render(request,'vendor/vendorsview.html',{'vendors':vendors})