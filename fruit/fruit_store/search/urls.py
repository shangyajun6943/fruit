from django.urls import path
from . import views
app_name = 'search'

urlpatterns = [
    path('key_search',views.key_search,name = 'key_search'),
    path('total_search',views.total_search,name='total_search'),
]
