from django.urls import path
from . import views

app_name='shopcart'

urlpatterns = [
    path('show', views.show,name='show'),
    path('place_order',views.place_order,name='place_order'),
    path('add_shopcart',views.add_shopcart,name='add_shopcart'),
    path('remove',views.remove,name='remove'),
]