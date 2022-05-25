import MySQLdb
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from gitdb.utils.encoding import force_text

from diplomaproject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from diplomaproject.tokens import generate_token

username = ""
fn = ""
ln = ""
email = ""
passwd = ""


def index(request):
    return render(request, 'main/index.html')


def signup(request):
    return render(request, 'signup/signup.html')


@csrf_protect
def signupaction(request):
    if request.method == "POST":
        username = request.POST['full_name']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['your_email']
        pass1 = request.POST['password']
        pass2 = request.POST['confirm_password']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('register')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('register')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('register')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('register')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = False
        myuser.save()
        messages.success(request,
                         "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email
        subject = "Welcome to Interactive Map by MKR- Django Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Interactive Map by MKR!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nKassymbayev Kuanysh"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ Interactive Map by MKR - Django Login!!"
        message2 = render_to_string('signup/email_confirmation.html', {

            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('login')

    return render(request, "signup/signup.html")

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
        context = {'uidb64': uidb64, 'token': token}
        return render(request, 'login/signin.html', context)
    else:
        return render(request,'activation_failed.html')


def signin(request):
    return render(request, 'main/index.html')


def login_as_guest(request):
    return render(request, 'main/index.html')