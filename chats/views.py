import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login as auth_login, logout
from chats.models import Chat, ChatAdmin, Message
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def register(request):
    if request.method == "POST":
        username = json.loads(request.body)["username"]
        fname = json.loads(request.body)['first_name']
        lname = json.loads(request.body)['last_name']
        email = json.loads(request.body)['email']
        pass1 = json.loads(request.body)['password1']
        pass2 = json.loads(request.body)['password2']

        if User.objects.filter(username=username):
            #messages.error(request, "Username already exist! Please try other username.")
            return JsonResponse({"status" : "unsuccessful",
                                "error": "Username already exist! Please try other username."})
    
        if User.objects.filter(email=email).exists():
            #messages.error(request, "Email is already registered!")
            return JsonResponse({"status" : "unsuccessful",
                                "error": "Email is already registered!"})
        
        try:
            validate_email(email)
        except:
            return JsonResponse({"status" : "unsuccessful",
                                "error": "Please enter valid email!"})
        
        if len(username) > 20:
            #messages.error(request, "Username must be under 20 characters!")
            return JsonResponse({"status" : "unsuccessful",
                                "error": "Username must be under 20 characters!"})
        
        if pass1 != pass2:
            #messages.error(request, "Passwords didn't matched!")
            return JsonResponse({"status" : "unsuccessful",
                                "error": "Passwords didn't matched!"})

        passReg = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
        pat = re.compile(passReg)
        if not re.search(pat, pass1):
            return JsonResponse({"status" : "unsuccessful",
                                "error": "Your password must contain at least one small letter, one capital letter, one number and must be at least 8 symbols long."})
        myusr = User.objects.create_user(username, email, pass1)
        myusr.first_name = fname
        myusr.last_name = lname
        myusr.is_active = True
        myusr.save()
        #messages.success(request, "Your account has been created succesfully!")
        return JsonResponse({"status" : "successful"})

@csrf_exempt
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
            return JsonResponse({'status':'successful',
                                    "id" : current_user.id,
                                    "password": current_user.password,
                                    "username": current_user.username,
                                    "email": current_user.email,
                                    "first_name": current_user.first_name,
                                    "last_name": current_user.last_name,
                                    "is_active": current_user.is_active})
        else:
            print("not logged")
            return JsonResponse({"status" : "unsuccessful"})

def log_out(request):
    logout(request)
    return redirect('index')

def chats_list(request):
    if request.method == "POST":
        pass

    return render(request, "chats_list.html") 
