from django.urls import path
from . import views

app_name='showcenter'

urlpatterns = [
    path('artic_show', views.artic_show,name='artic_show'),
    path('vedio_show',views.vedio_show,name='vedio_show'),


]