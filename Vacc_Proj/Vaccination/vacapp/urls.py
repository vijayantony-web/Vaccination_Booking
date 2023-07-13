from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from vacapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('hello/',views.hello,name='hello'),
    path('booklist/',views.booklist,name='booklist'),
    path('cart/',views.cart,name='cart'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]