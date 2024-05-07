from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
# Create your views here.

def ItemView(request):
    item = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    query = request.GET.get('query', '')

    if category_id:
        item = item.filter(category_id=category_id)

    if query:
        item = item.filter(Q(name__icontains = query) | Q(description__icontains=query))

    return render(request, 'item/item.html', {
        'items': item,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def Detail(request, pk):
    item = get_object_or_404(Item, id=pk)
    related_items = Item.objects.filter(category=item.category, is_sold = False).exclude(pk=pk)[:5]

    return render(request, "item/detail.html", {
        'item': item,
        'related_items': related_items,
        })

@login_required
def New_Item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            ''' doesnt save yet because it lacks the created_by field '''
            item = form.save(commit=False)
            item.created_by = request.user
            item.is_sold = False
            item.save()

            return redirect('item:detail', pk=item.id)
    else: 
        form = NewItemForm()

    return render(request, 'item/item_form.html', {
        'form': form,
        'title': 'New Item'
    })

@login_required
def Edit_Item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else: 
        form = EditItemForm(instance=item)

    return render(request, 'item/item_form.html', {
        'form': form,
        'title': 'Edit Item'
    })


@login_required
def Delete(request, pk): 
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:dashboard')