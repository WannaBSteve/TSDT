from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item
from django.shortcuts import redirect

from lists.models import Item, List



def new_list(request):
    list_user = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_user)
    return redirect(f'/lists/the-new-page/')

def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-new_page/')
# Create your views here.
