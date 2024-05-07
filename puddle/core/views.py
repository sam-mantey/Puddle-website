from django.shortcuts import render, redirect
from django.urls import reverse
from item.models import Category, Item
from .forms import SignupForm
# Create your views here.

def Index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        "items": items,
        "categories": categories,
    })

def Contact(request):
    return render(request, "core/contact.html")


def SignUp(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse("core:login"))
    
    else: 
        form = SignupForm()



    return render(request, 'core/signup.html', {"form": form})