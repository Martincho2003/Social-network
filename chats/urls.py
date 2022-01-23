from os import name
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'chats', views.ChatView, 'chat')

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.log_out, name='logout'),
    path('api/', include(router.urls)),
]