from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from django.utils import timezone

# Create your views here.
def home(request):
    products = Products.objects
    return render(request, 'products/products.html', {'products': products})
    
def detail(request, products_id):
    product = get_object_or_404(Products, pk=products_id)
    return render(request, 'products/detail.html', {'product': product})


def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['image'] and request.FILES['icon']:
        
        
            product = Products()
            product.title = request.POST['title']
            product.body = request.POST['body']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
               
               product.url= request.POST['url']
            else:
               product.url='http://' + request.POST['url']
               product.icon = request.FILES['icon']
               product.image = request.FILES['image']
               product.pub_date = timezone.datetime.now()
               product.hunter = request.user
               product.save()
            return redirect ('/products/' + str(product.id))
        else:
            return render(request,'products/toevoegen.html', {'error':'niet alle velden zijn ingevuld.'})

    else:
        return render(request,'products/toevoegen.html')    