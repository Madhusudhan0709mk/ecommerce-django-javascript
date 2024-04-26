from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'index.html',{'products':products})

def shopdetail(request):
    return render(request,'shopdetail.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')



def shop(request):
    return render(request,'shop.html')