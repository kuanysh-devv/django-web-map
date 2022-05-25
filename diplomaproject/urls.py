from django.contrib import admin
from django.urls import path, include
from signup.views import signupaction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
