import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login as auth_login, logout
from chats.models import Chat, ChatAdmin, ChatMember, Message
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
        user = authenticate(request, username=usrname, password=password)
        if user is not None:
            auth_login(request, user)
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
            return JsonResponse({"status" : "unsuccessful"})

def log_out(request):
    logout(request)
    return redirect('index')

@csrf_exempt
def create_chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        member_count = data["members_count"]
        if Chat.objects.filter(chat_name=data["chat_name"], chat_owner=request.user).count() == 0:
            Chat.objects.create(chat_name=data["chat_name"], chat_memebers_count=member_count, chat_owner=request.user).save()
            new_chat = Chat.objects.get(chat_name=data["chat_name"], chat_owner=request.user.id)
            for member in data["usernames"]:
                ChatMember.objects.create(chat=new_chat, member=User.objects.get(username=member["username"])).save()
            return JsonResponse({"status": "successful"})
        return JsonResponse({"status": "unsuccessful", "error": "Chat already exists!"})
        
def chats_list(request):
    if request.method == "GET":
        chats = Chat.objects.filter(chat_owner = request.user.id).values()
        chat_resp = {"chats": []}
        for chat in chats:
            chat_resp["chats"].append({"chat_name": chat["chat_name"], "chat_owner_id": chat["chat_owner_id"]})
    
        return JsonResponse(chat_resp)

def search_users(request):
    if request.method == "GET":
        all_users = User.objects.all().values()
        searched_string = json.loads(request.body)["string"]
        users_resp = {"users": []}
        for user in all_users:
            if user["username"].lower().find(searched_string) != -1:
                users_resp["users"].append({"username": user["username"]})
        return JsonResponse(users_resp)

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        data = json.loads(request.body)
        chat_name = data["chat_name"]
        chat_ownder_id = data["chat_owner_id"]
        chat = Chat.objects.get(chat_name=chat_name, chat_owner=chat_ownder_id)
        text = data["message_text"]
        Message.objects.create(message_text=text, sender=request.user, chat=chat).save()
        return JsonResponse({"status": "successful"})

def load_messages(request):
    if request.method == "GET":
        data = json.loads(request.body)
        chat_name = data["chat_name"]
        chat_ownder_id = data["chat_owner_id"]
        chat = Chat.objects.get(chat_name=chat_name, chat_owner=chat_ownder_id)
        messages_resp = {"messages": []}
        messages = Message.objects.filter(chat=chat.id).values()
        for message in messages:
            sender = User.objects.get(id=message["sender_id"])
            messages_resp["messages"].append({"message_text": message["message_text"],
                                                "sender": sender.username})

        return JsonResponse(messages_resp)

@csrf_exempt
def add_user_to_chat(request):
     if request.method == "POST":
        data = json.loads(request.body)
        chat_name = data["chat_name"]
        chat_ownder_id = data["chat_owner_id"]
        chat = Chat.objects.get(chat_name=chat_name, chat_owner=chat_ownder_id)
        new_username = data["username"]
        ChatMember.objects.create(chat=chat, member=User.objects.get(username=new_username)).save()
        
        return JsonResponse({"status": "successful"})