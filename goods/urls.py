from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('get_token', views.get_token, name='get_token'),
    path('get_token/', views.get_token, name='get_token'),
    path('goods', views.view_goods, name='goods'),
    path('new_good', views.Goods_api.as_view(), name='goods_api')
]