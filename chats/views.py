from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout


def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        username = request.POST['usrname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try other username.")
            return redirect('register')
    
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return redirect('register')
        
        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters!")
            return redirect('register')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!")
            return redirect('register')

        myusr = User.objects.create_user(username, email, pass1)
        myusr.first_name = fname
        myusr.last_name = lname
        myusr.is_active = True
        myusr.save()
        messages.success(request, "Your account has been created succesfully!")
        return redirect("login")

    return render(request, "register.html") 

def login(request):
    if request.method == "POST":
        username = request.POST['usrname']
        password = request.POST['pass']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print("logged")
            return render(request, "index.html", {'fname': username})
            ...
        else:
            print("not logged")
            return render(request, "index.html", {'fname': username})
            ...
    else:
       return render(request, "login.html") 

def log_out(request):
    logout(request)
    return redirect('index')