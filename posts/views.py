from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from posts.models import Post
# Create your views here.
def new(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            user = request.user
            body = request.POST['body']
            title = request.POST['title']
            post = Post.objects.create(user=user, body=body, title=title)
            return redirect(reverse("posts:detail", args=(post.id,)))
        else:
            return render(request, "posts/new.html")
    else:
        return redirect(reverse('home'))

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "posts/detail.html", {"post":post})
