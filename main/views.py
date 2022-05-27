from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
import pandas as pd
import pyodbc
import geojson
import json

from djgeojson import serializers
from geojson import Feature, FeatureCollection, Point
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from gitdb.utils.encoding import force_text

from . tokens import generate_token
from diplomaproject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import Places, Shop, Product
from django.core.serializers import serialize


def places_datasets(request):
    places_data=serialize('geojson', Places.objects.all())
    return HttpResponse(places_data, content_type='application/json')


def index(request):

    return render(request, 'main/index.html')


def to_search_page(request):
    return render(request, 'main/search_page.html')


def signup(request):
    return render(request, 'signup/signup.html')


def signin(request):
    return render(request, 'login/signin.html')


def login_as_guest(request):
    return render(request, 'main/index.html')


def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")

        return redirect('login')
    else:
        return render(request,'activation_failed.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')


def Print_ListView(request):
    json_serializer = serializers.get_serializer("json")()
    shops = json_serializer.serialize(Shop.objects.all(), ensure_ascii=False)
    return render(request, 'index.html', {'shops': shops});


def Print_products(request):
    products = Product.objects.all()
    return render(request, 'main/search_page.html', {'products_list': products});

def search(request):
    query = None
    results=[]
    if request.method == "GET":
        query = request.GET.get('search')
        results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request,'main/search_page.html',{'query': query, 'results': results})

