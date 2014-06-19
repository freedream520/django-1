from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from posts.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.exceptions import PermissionDenied

# Create your views here.
@login_required
def new(request):
    if request.method == "POST":
        user = request.user
        body = request.POST['body']
        if not body.strip():
            return redirect(reverse('home'))
        title = request.POST['title']
        post = Post.objects.create(user=user, body=body, title=title)
        return redirect(reverse('home'))
    else:
        return render(request, "posts/new.html")

@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    body = post.body
    return render(request, "posts/detail.html", {"post":post})

@login_required
def delete(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        if post.user == request.user:
            post.delete()
            return redirect(reverse('home'))
        else:
            raise PermissionDenied
    else:
        raise Http404

@login_required
def comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        body = request.POST['body']
        if not body.strip():
            return redirect(reverse('home'))
        comment = Comment.objects.create(user=user, body=body, post=post)
        return redirect(reverse('home'))
    else:
        raise Http404
