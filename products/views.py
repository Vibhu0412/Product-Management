from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

# Create your views here.

from . models import Product, Category
from . forms import ProductForm


@login_required(login_url='accounts/login')
def ShowAllProducts(request):

    category = request.GET.get('category')

    if category == None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category__name=category)



    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'showProducts.html', context)



@login_required(login_url='showProducts')
def productDetail(request, pk):
    eachProduct = Product.objects.get(id=pk)


    context = {
        'eachProduct': eachProduct
    }

    return render(request, 'productDetail.html', context)


@login_required(login_url='showProducts')
def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')
    else:
        form = ProductForm()

    context = {
        "form":form
    }

    return render(request, 'addProduct.html', context)


@login_required(login_url='showProducts')
def updateProduct(request,pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = {
        "form":form
    }

    return render(request, 'updateProduct.html', context)



@login_required(login_url='showProducts')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('showProducts')