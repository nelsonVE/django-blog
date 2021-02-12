from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, PostForm
from django.contrib import messages
from .models import User, Post
from Lib import datetime

def index(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, 'blog/index.html', { 'posts': posts })

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = { 'form': form }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username, password = password)

            if user is None:
                messages.error(request, "User or password not valid")
                return render(request, 'blog/login.html', context)
            else:
                messages.success(request, "User successfully logged in")
                login(request, user)
                return redirect(reverse("blog:index"))

    return render(request, 'blog/login.html', context)

@login_required(login_url="blog:login")
def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(reverse("blog:index"))

@login_required(login_url="blog:login")
@permission_required("blog.post")
def postCreate(request):
    """""
    Function that creates new post, only allowed to admins.
    """""

    form = PostForm(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")

            post = Post(title = title, content = content, user_id = request.user.id, created_at = datetime.datetime.now().date())
            post.save()

            if post is not None:
                messages.success(request, "Post created successfully")
                return redirect(reverse("blog:index"))
            else:
                messages.error(request, "An error has been ocurred while trying to create the post")


    return render(request, "blog/create_post.html", context)

@login_required(login_url="blog:login")
def postView(request, post_id):
    """""
    Get the actual post and the last 5 posts created.
    """""
    actual_post = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.all().order_by("-created_at")[:5]
    return render(request, "blog/view_post.html", { 'actual_post': actual_post, 'posts': posts })

@login_required(login_url="blog:login")
@permission_required("blog.post")
def postUpdate(request, post_id):
    """""
    Function that updates a post, only allowed to admins.
    """""
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance = post)
    context = {
        'form': form
    }

    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit = False)
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")

            post.user_id = request.user.id
            post.title = title
            post.content = content

            post.save(update_fields=['user', 'title', 'content'])

            if post is not None:
                messages.success(request, "Post updated successfully")
                return redirect(reverse("blog:postView", kwargs={'post_id': post_id}))
            else:
                messages.error(request, "An error has been ocurred while trying to update the post")


    return render(request, "blog/create_post.html", context)

@login_required(login_url="blog:login")
@permission_required("blog.post")
def postDelete(request, post_id):
    """""
    Function that deletes a post, only allowed to admins.
    """""
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, "Post deleted successfully")

    return redirect(reverse("blog:index"))