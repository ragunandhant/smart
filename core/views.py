from django.shortcuts import render
from food.models import Category, Item

def index(request):
    categories = Category.objects.all()
    category_items = {}
    for category in categories:
        items = Item.objects.filter(category=category)
        category_items[category.name] = items
    
    return render(request, 'index.html', {'categories': categories, 'category_items': category_items})

