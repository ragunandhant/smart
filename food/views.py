from django.shortcuts import render,get_object_or_404
from .models import Item
from .models import Category,Item
# Create your views here.
def detail(request,pk):
    category_selected = get_object_or_404(Category,pk = pk)
    related_tem = Item.objects.filter(category=category_selected)
    print(related_tem)
    return render(request,'item/detail.html',{'related_item':related_tem})