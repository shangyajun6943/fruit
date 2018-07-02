from django.shortcuts import render

# Create your views here.


def key_search(request):
    return render(request,'showgoods/product_list.html')


def total_search(request):
    return render(request,'showgoods/product_list.html'),