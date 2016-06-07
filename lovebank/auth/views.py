from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.admin import User

# Create your views here.


def my_login(request):
    if request.POST["login"]:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                HttpResponseRedirect("/Dashboard/")
            else:
               context = {
                   "title": "login",
                   "massage": "Please active your account via the link we sent to your email, thanks."
               }
        else:
            context = {
                "title": "login",
                "massage": "The information you inter is not valid"
            }
    return render(request, "login.html", context)


def my_register(request):
    if request.POST["login"]:
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        email = request.POST["email"]
        if (request.POST["username"] != request.POST["repassword"]):
            context = {
                "title": "Register",
                "massage": "User already exist"
            }

        render(request, "register.html", context)
        if (User.objects.filter(email=email).exists()) or (User.objects.filter(email=username).exists()):
            context = {
                "title": "Register",
                "massage": "User already exist"
            }
        render(request, "register.html", context)

        user = User(username=username, password=password, email=email)
        user.save()

