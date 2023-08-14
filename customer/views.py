from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Sum
from django.db.models.query import Q

from customer.models import Customer,Usage


# Create your views here.
def showview(request):
   # items=Usage.items.filter(customer__name__icontains='k')
   # items=Usage.usage_items.annotate(sum_usage = Sum('usage'))
    items=Usage.usage_items.filter(Q(customer__name ='K1' ) | Q(customer__name ='test1'))
    return render(request,'Atena.html',{'items' : items})
    # response =HttpResponse()
    # response.write('<h1>Hello</h1>')
    # return  response
