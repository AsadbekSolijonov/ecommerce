from django.shortcuts import render, get_object_or_404

from store.models import Product


# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    context = {
        "product": products
    }
    return render(request, 'store/detail.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

