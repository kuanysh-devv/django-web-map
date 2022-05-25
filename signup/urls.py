from django.urls import path

from login.views import signinaction
from . import views
from signup.views import signupaction

urlpatterns = [
    path('', signinaction, name='login'),
    path('home/', views.index, name='home'),
    path('sign-up/', signupaction, name='register'),
    path('sign-in/', signinaction, name='login'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('login-as-guest', views.login_as_guest, name='login_as_guest')
]