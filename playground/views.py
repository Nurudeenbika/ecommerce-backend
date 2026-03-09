from django.shortcuts import render
from django.http import HttpResponse, render

from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()

    for product in query_set:
        print(product)
#    queryset = Product.objects.filter(unit_price__gt=20)
    return render(request, 'hello.html', {'name': 'Nuru', 'products': queryset})
