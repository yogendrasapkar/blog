from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.helloWorld, name='helloWorld'),
    # path('page', views.index, name='index')
    path('index',views.index,name='index'),
    path('register', views.register, name='register'),
    path('login', views.signin, name='signin'),
    path('logout',views.userLogout,name='userLogout'),
     path('profile',views.userProfile,name='userProfile')

]