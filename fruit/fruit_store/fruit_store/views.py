from django.shortcuts import render
from django.contrib.sessions.models import Session
import json
from account.models import *
from untils.getinfo import *

# Create your views here.
def index(request):
    #首页-获取用户信息
    user=getUser(request)
    #首页获取产品列表
    goodslist=getIndexGoods()
    return render(request,'index.html',{'userinfo':user,'goodslist':goodslist})