from django.urls import path, re_path

import login.views
import main.views
from login.views import signinaction
from signup.views import signupaction
from . import views

urlpatterns = [
    path('', login.views.signin),
    path('home/', views.index, name='home'),
    path('sign-up/', signupaction, name='register'),
    path('sign-in/', signinaction, name='login'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('login-as-guest', views.login_as_guest, name='login_as_guest'),
    path('signout', views.signout, name='signout'),
    path('search-page/', views.to_search_page, name='to_search'),
    path('products', main.views.Print_products, name='Print_products'),
    path('search/', main.views.search, name='search'),

]