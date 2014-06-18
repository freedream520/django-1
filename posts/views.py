from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from posts.models import Post
from django.contrib.auth.decorators import login_required
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
