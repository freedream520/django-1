from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
def home(request):
    return render(request, 'home/index.html')

def login_view(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'home/login.html', {'error_message':"User is not active"})
        else:
            return render(request, 'home/login.html', {'error_message':"invalid login"})
    except KeyError:
        return render(request, 'home/login.html')

def register(request):
    return render(request, 'home/register.html')
