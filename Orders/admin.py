from django.contrib import admin

from Orders.models import SalesOrder
from Products.models import Product

admin.site.register(SalesOrder)
