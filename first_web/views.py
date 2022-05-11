from argparse import _MutuallyExclusiveGroup
import email
from email import message
from http.client import HTTPResponse
from imaplib import _Authenticator
from multiprocessing import AuthenticationError
from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout


# Create your views here.


def home(request):
    return render(request, "first_web/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Accout has been Successfully Created")

        return redirect('signin')

    return render(request, "first_web/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "first_web/index.html", {'fname': fname})
        else:
            message.error(request, "Bad Credentials!")
            return redirect('home')


def signin(request):
    return render(request, "first_web/signin.html")


def signout(request):
    logout(request)
    message.success(request, "Logged out Successfully!")
    return redirect('home')
