import MySQLdb
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from gitdb.utils.encoding import force_text

from diplomaproject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout

from main.tokens import generate_token

username = ""
passwd = ""


def index(request, fname):

    return render(request, 'main/index.html', {'fname': fname})


def signup(request):
    return render(request, 'signup/signup.html')


def signin(request):
    return render(request, 'login/signin.html')


@csrf_exempt
def signinaction(request):
    if request.method == 'POST':
        username = request.POST['full_name_1']
        pass1 = request.POST['password_1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            #messages.success(request, "Logged In Sucessfully!!")
            #return render(request, "main/index.html", {"fname": fname})
            request.session['fname'] = fname
            return redirect('/home', fname=fname)

        else:
            messages.error(request, "Bad Credentials!!")
            return render(request, "login/signin.html")

    return render(request, "login/signin.html")

@csrf_exempt
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')


@csrf_exempt
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
        return render(request, 'login/signin.html')
    else:
        return render(request,'activation_failed.html')

def login_as_guest(request):
    return render(request, 'main/index.html')
