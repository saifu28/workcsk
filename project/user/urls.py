from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [

    path('expage', views.expage, name="expage"),
    path('home', views.home, name="home"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name='signup'),
    path('shop', views.shop, name="shop"),
    path('info', views.info, name="info")

]
