from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth import authenticate, login, register, logout


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

"""def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        ...
    else:
        # Return an 'invalid login' error message."""
