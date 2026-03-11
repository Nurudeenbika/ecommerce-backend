from django.shortcuts import render
from django.db import connection
from store.models import Product, Order, OrderItem, Customer, Collection


def say_hello(request):
    with connection.cursor() as cursor:
        cursor.execute()

    return render(request, 'hello.html', {'name': 'Nuru', 'result': list(queryset)})
