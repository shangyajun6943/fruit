from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import *
from .models import User 
import json
# Create your views here.



def login(request):
    return render(request,'account/login.html')

def dologin(request):
    username=request.POST['username']
    pwd=request.POST['pwd']
    try:
        user=User.users.get(username=username,passwd=pwd)
    except Exception as e:
        return redirect('account:login')

    user1 = json.dumps(user, default=lambda obj: obj.__dict__)
    print(user1)
    request.session['userinfo']=user1
    # a = request.session['userinfo']=user1
    # print(a)
    return redirect( 'index')

def outlogin(request):
    '''
        注销
    '''
    if request.session['userinfo']:
        request.session.flush()
        return redirect('index')
    else:
        return HttpResponse('error')

def register(request):
    return render(request,'account/register.html')

def do_register(request):
    #用户名
    username=request.POST['user_name']
    # 密码1
    password1=request.POST['pwd']
    # 密码2
    password2=request.POST['cpwd']
    #email
    email=request.POST['email']
    #判断用户是否存在
    user=User.users.filter(username=username)
    if not user:
        #不存在此用户
        user=User()

        user.username=username
        
        user.passwd=password2

        user.email=email

        user.save()
        user1=User.users.get(username=username)
        
        u=json.dumps(user1,default=lambda obj:obj.__dict__)

        request.session['userinfo']=u

        return redirect('index')
        
    return HttpResponse('用户已存在')# ？？

def user_center(request):
    '''
        用户详情
    '''
    return render(request,'account/user_center_info.html')

def user_center_order(request):
    '''
        用户订单
    '''
    return render(request,'account/user_center_order.html')
def user_center_site(request):
    '''
        用户详情
    '''
    return render(request,'account/user_center_site.html')