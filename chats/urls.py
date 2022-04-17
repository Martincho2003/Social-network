from os import name
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'chats', views.ChatView, 'chats')
router.register(r'chatadmins', views.ChatAdminView, 'chatadmins')
router.register(r'messages', views.MessageView, 'messages')
router.register(r'users', views.UserView, 'users')

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.log_out, name='logout'),
    path('chats-list', views.chats_list),
    path('create-chat', views.create_chat),
    path('search-user', views.search_users),
    path('send-message', views.send_message),
    path('load-messages', views.load_messages),
    path('add-user-to-chat', views.add_user_to_chat),
    path('api/', include(router.urls)),
]