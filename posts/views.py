from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from posts.models import Post, Comment
from notifications.models import Notification
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
        return redirect(reverse("posts:detail", kwargs={'post_id':post.id}))
    else:
        return render(request, "posts/new.html")

@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    body = post.body
    return render(request, "posts/detail.html", {"post":post})

@login_required
def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user != request.user:
        raise PermissionDenied
    elif request.method == "POST":
        body = request.POST['body']
        if not body.strip():
            return render(request, "posts/edit.html", {"post":post})
        post.body = body
        post.save()
        return redirect(reverse("posts:detail", kwargs={'post_id':post.id}))
    else:
        return render(request, "posts/edit.html", {"post":post})

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user == request.user:
        post.delete()
        return redirect(reverse('home'))
    else:
        raise PermissionDenied

@login_required
def comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        user = request.user
        body = request.POST['body']
        if not body.strip():
            return redirect(reverse('home'))
        comment = Comment.objects.create(user=user, body=body, post=post)
        info_text = "%s commented on your post" % user.username
        link_text = reverse("posts:detail", kwargs={'post_id':post.id})
        notified = {}
        if user != post.user:
            print "Notification"
            notified[post.user] = True
            note = Notification.objects.create(user=post.user, info=info_text, link=link_text)
        info_text = "%s commented on a post you are following" % user.username
        for cmnt in post.comment_set.all():
            if cmnt.user != user and not cmnt.user in notified:
                print "Notification"
                note = Notification.objects.create(user=cmnt.user, info=info_text, link=link_text)
                notified[cmnt.user] = True
        return redirect(reverse("posts:detail", kwargs={'post_id':post.id}))
    else:
        raise Http404
