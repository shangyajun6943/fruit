from account.models import *
import json
from showgoods.models import *

def getUser(request):
    '''
        从session中获取登录后的用户信息
    '''
    try:
        sess2=json.loads(request.session['userinfo'])
    except Exception as e:
        print(e)
        return None
    #把字典转换成对象
    user=User()
    user.__dict__=sess2
    return user

def getIndexGoods():
    '''
        首页的产品信息的展示代码
    '''
    products=[]
    list1=[10,20,30,40,50,60]
    for i in list1:
        products1=list(Goods.goods.filter(isDelete=0,goods_status=1,goods_type__range=[i-10,i]).order_by('-shopping_state')[0:4])
        # print(products1)
        products.append((int(i/10),products1))
    return products
