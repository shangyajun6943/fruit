from django.shortcuts import render
from untils.getinfo import *
from .models import *

# Create your views here.


def detial(request,gid=None):
    if gid is None:
        return render(request,'404.html')
    #那用户信息
    user=getUser(request)
    #商品信息
    good=Goods.goods.get(pk=int(gid))
    return render(request,'showgoods/detial.html',{'userinfo':user,'good':good})

def productlist(request,type1=None):
    if type1 is None:
        return render(request,'404.html')
    #商品类型
    num=int(type1)*10
    #那用户信息
    user=getUser(request)
    #商品信息
    good=list(Goods.goods.filter(goods_type__range=[num-10,num]))
    return render(request, 'showgoods/product_list.html',{'userinfo':user,'good':good})
