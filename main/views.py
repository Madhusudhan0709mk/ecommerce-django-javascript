from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def shopdetail(request):
    return render(request,'shopdetail.html')

def cart(request):
    return render(request,'cart.html')


def checkout(request):
    return render(request,'checkout.html')



def shop(request):
    return render(request,'shop.html')