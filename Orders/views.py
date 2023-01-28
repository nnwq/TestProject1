from django.shortcuts import render
from Orders.models import SalesOrder


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})
