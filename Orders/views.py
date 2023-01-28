from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from Orders.models import SalesOrder
from Orders.serializers import OrderSerializer


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer

