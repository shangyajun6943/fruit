from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('login', views.login,name='login'),
    path('dologin', views.dologin,name='dologin'),
    path('outlogin', views.outlogin,name='outlogin'),
    path('register',views.register,name='register'),
    path('do_register',views.do_register,name='do_register'),
    path('user_center',views.user_center,name='user_center'),
    path('user_center_order',views.user_center_order,name='user_center_order'),
    path('user_center_site',views.user_center_site,name='user_center_site'),

]