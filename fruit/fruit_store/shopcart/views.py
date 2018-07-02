from django.shortcuts import render
from django.http import HttpResponse
from django.conf import *
from shopcart.shopcart import *
from untils.getinfo import *
from .models import *
from django.contrib.sessions.models import Session
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def show(request):
    '''
        购物车显示
    '''
    # 判断是否登录
    user=getUser(request)
    if user is None:
        return render(request, 'account/login.html')
    #用户存在
    #创建购物车
    shopcart=ShopCart()
    #检查订单
    order=list(Order.orders.all().filter(userid=user.id,isdelete=0))
    if order:
        #如果订单存在
        order = order[0]
        # print(order)
        if not bool(order):
            return render(request, 'shopcart/shopcart.html', {"shopcart": shopcart,'userinfo':user})
        else:
            shopcart.order=order
            list1=[]
            #获取订单的订单ID-查找订单项
            order_id = order.id
            #由当天的订单的id查询获取isdelete=0的订单项
            shop_user = list(Shop_user.shops.all().filter(id=shopcart.order.shopid_id))
            # print(shop_user)
            shop_user=shop_user[0]
            shopcart.shop_user=shop_user
            items=list(Order_item.orderitem.all().filter(order_id=order_id,isdelete=0))
            if not bool(items):
                shopcart.order_item_list=list1
                return render(request, 'shopcart/shopcart.html', {"shopcart": shopcart,'userinfo':user})
            else:
                for item in items:
                    list_item = OrderItems()
                    list_item.order_item=item
                    #订单项id/产品信息
                    product=item.pro_id
                    list_item.product=product
                    #获取单个订单项总价
                    item_subtotal=list_item.product.price*list_item.order_item.quantity
                    #将总价加给order_item
                    list_item.order_item.subtotal=item_subtotal
                    #获取总价
                    list1.append(list_item)
                shopcart.order_item_list=list1

        quantity = json.dumps(list_item.order_item.quantity, default=lambda obj: obj.__dict__)
        request.session['order_item_list'] = quantity
        # print(quantity)
        return render(request,'shopcart/shopcart.html',{"shopcart":shopcart,'userinfo':user})
    else:
        return render(request, 'shopcart/shopcart.html', {"shopcart": shopcart,'userinfo':user})



def place_order(request):
    return render(request,'shopcart/place_order.html')

def add_shopcart(request):
    proid=request.POST['pro_id']
    print(proid)
    num=request.POST['num']
    print(num)
    if proid is None:
        return HttpResponse(0)
    else:
        #检测用户是否登录
        try:
            #获取用户信息
            user=getUser(request)
            #获取用户对象
            user2=User.users.get(pk=user.id)
        except AttributeError as e:
            print(e)
            return HttpResponse(2)
        #获取商铺对象
        shop=Shop_user.shops.get(pk=1)
        #获取商品
        goods=Goods.goods.get(pk=int(proid))
        #获取当前时间的年月日
        year=datetime.now().year
        month=datetime.now().month
        day=datetime.now().day
        order=Order.orders.filter(isdelete=0,userid=user.id)
        if not bool(list(order)):
            # 创建新订单
            order=Order()
            time1=str(time.time())
            order_number=time1[0:10]+time1[11:]+str(goods.goods_volume)+str(goods.goods_num)
            order.order_number=order_number
            order.userid=user2
            order.shopid=shop
            order.order_time=datetime(year,month,day)
            order.delivery_time=datetime.now()
            order.shopping_state=0
            order.save()
        # 创建新订单项
        order_item=Order_item()
        order_item.pro_id=goods
        try:
            order_item.order_id=list(order)[0]
        except TypeError as e:
            print(e)
            order_item.order_id=order
        order_item.quantity=int(num)
        order_item.save()
        return HttpResponse(1)
    return render(request,'shopcart/shopcart.html')

@csrf_exempt
def remove(request):
    ordid=request.POST['orderid']
    print(ordid)
    orderitem=Order_item.orderitem.get(pk=int(ordid))
    orderitem.isdelete=1
    orderitem.save()
    return HttpResponse(1)