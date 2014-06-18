from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from posts.models import Post
from django.contrib.auth.decorators import login_required

def home(request):
    user_list = None
    post_list = None
    if request.user.is_authenticated():
        user_list = User.objects.all()
        post_list = Post.objects.all().order_by('-pub_date')
    return render(request, 'home/index.html', {'user_list':user_list, 'post_list':post_list})

def login_view(request):
    if request.user.is_authenticated():
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.user = user
                return redirect(reverse('home'))
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

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def user_page(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    post_set = user.post_set.all().order_by('-pub_date')
    return render(request, 'home/user.html', {'profile':user, 'post_set':post_set})

@login_required
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
