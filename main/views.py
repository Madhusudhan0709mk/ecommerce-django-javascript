from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
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
    # Retrieve the product based on pid
    product = get_object_or_404(Product, pid=pid)
    return render(request, 'products/product_detail_view.html', {'product': product})

def increment_quantity(request, pid):
    if request.method == 'POST':
        # Retrieve the product based on pid
        product = Product.objects.get(pid=pid)
        
        # Increment the quantity by 1
        product.quantity += 1
        product.save()
        
        # Optionally, you can show a success message
        messages.success(request, 'Quantity incremented successfully!')
        
        # Redirect the user back to the product detail page
        return redirect('product_detail_view', pid=pid)

def shopdetail(request):
    return render(request,'shopdetail.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')



def shop(request):
    return render(request,'shop.html')