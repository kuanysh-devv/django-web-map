from django.urls import path

import login.views
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
    path(r'^places_data/$',views.places_datasets,name='place'),

    path('^all_shops$', views.Print_ListView)

]