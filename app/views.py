from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request,'index.html')

def home_page(request):
    return render(request,'home.html',{
        'new_item_text':request.POST.get('item_text',''),
    })