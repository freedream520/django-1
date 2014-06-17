from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    user_list = None
    if request.user.is_authenticated():
        user_list = User.objects.all()
    return render(request, 'home/index.html', {'user_list':user_list})

def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.user = user
                return HttpResponseRedirect('/')
            else:
                return render(request, 'home/index.html',{'error_message':"User is not active"})
        else:
            return render(request, 'home/index.html', {'error_message':"invalid login"})
    else:
        return render(request, 'home/index.html')

def register(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        try:
            if User.objects.get(username__exact=username) is not None:
                return render(request, 'home/index.html', {'error_message':"username is not available"})
        except:
            pass
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'home/index.html')

def logout_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            logout(request)
        return redirect('/')
    else:
        return redirect('/')

def user_page(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'home/user.html', {'profile':user})

def user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if (request.user.is_authenticated()) and (request.user == user):
        if request.method == 'POST':
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            if fname:
                user.first_name = fname
            if lname:
                user.last_name = lname
            if email:
                user.email = email
            user.save()
            return redirect(reverse('user', args=(user_id)))
        else:
            return render(request, 'home/edit_user.html')
    else:
        return redirect(reverse('user', args=(user_id)))
