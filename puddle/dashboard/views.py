from django.shortcuts import render
from item.models import Item
# Create your views here.

def Dashboard(request): 
    items = Item.objects.filter(created_by = request.user)

    return render(request, 'dashboard/dashboard.html', {
        "items" : items,
    })
