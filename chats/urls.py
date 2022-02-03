from os import name
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'chats', views.ChatView, 'chat')
<<<<<<< HEAD
router.register(r'chatadmin', views.ChatAdminView, 'chatadmin')
router.register(r'message', views.MessageView, 'message')
router.register(r'user', views.UserView, 'user')
=======
>>>>>>> master

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.log_out, name='logout'),
    path('api/', include(router.urls)),
]