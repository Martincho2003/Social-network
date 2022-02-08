import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login as auth_login, logout
from chats.models import Chat, ChatAdmin, Message

from rest_framework import viewsets
from .serializers import ChatSerializer, ChatAdminSerializer, MessageSerializer, UserSerializer

class ChatView(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

class ChatAdminView(viewsets.ModelViewSet):
    serializer_class = ChatAdminSerializer
    queryset = ChatAdmin.objects.all()

class MessageView(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

def index(request):
    if not request.user.is_anonymous:
        current_user = request.user

        rooms = Chat.objects.filter(chat_owner = current_user.id)

        if type(rooms) == list:
            chat_rooms = []
            chat_rooms.append(rooms)
            return render(request, "index.html", {"rooms" : chat_rooms})
            
        return render(request, "index.html", {"rooms" : rooms})

    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if User.objects.filter(username=username):
            #messages.error(request, "Username already exist! Please try other username.")
            return JsonResponse({"status" : "unsuccessfull",
                                "error": "Username already exist! Please try other username."})
    
        if User.objects.filter(email=email).exists():
            #messages.error(request, "Email is already registered!")
            return JsonResponse({"status" : "unsuccessfull",
                                "error": "Email is already registered!"})
        
        try:
            validate_email(email)
        except:
            return JsonResponse({"status" : "unsuccessfull",
                                "error": "Please enter valid email!"})
        
        if len(username) > 20:
            #messages.error(request, "Username must be under 20 characters!")
            return JsonResponse({"status" : "unsuccessfull",
                                "error": "Username must be under 20 characters!"})
        
        if pass1 != pass2:
            #messages.error(request, "Passwords didn't matched!")
            return JsonResponse({"status" : "unsuccessfull",
                                "error": "Passwords didn't matched!"})

        passReg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
        pat = re.compile(passReg)
        if not re.search(pat, pass1):
            return JsonResponse({"status" : "unsuccessfull",
                                "error": "Your password must contain at least one small letter, one capital letter, one number, one special symbol and must be at least 8 symbols long."})

        myusr = User.objects.create_user(username, email, pass1)
        myusr.first_name = fname
        myusr.last_name = lname
        myusr.is_active = True
        myusr.save()
        #messages.success(request, "Your account has been created succesfully!")
        return JsonResponse({"status" : "successfull"})

def login(request):
    if request.method == "POST":
        usrname = json.loads(request.body)["username"]
        password = json.loads(request.body)['password']
        print(password)
        user = authenticate(request, username=usrname, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            print("logged")
            current_user = request.user
            return JsonResponse({'status':'successfull',
                                    "id" : current_user.id,
                                    "password": current_user.password,
                                    "username": current_user.username,
                                    "email": current_user.email,
                                    "first_name": current_user.first_name,
                                    "last_name": current_user.last_name,
                                    "is_active": current_user.is_active})
        else:
            print("not logged")
            return JsonResponse({"status" : "unsuccessfull"})

def log_out(request):
    logout(request)
    return redirect('index')

def chats_list(request):
    if request.method == "POST":
        pass

    return render(request, "chats_list.html") 