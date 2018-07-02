from django.urls import path
from . import views

app_name='showgoods'

urlpatterns = [
    path('detial/(?P<gid>[0-9]{1-4})', views.detial,name='detial'),
    path('productlist/(?P<type1>[0-9])', views.productlist,name='productlist'),
]