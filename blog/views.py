from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, reverse
from .forms import LoginForm, PostForm
from django.contrib import messages
from .models import User, Post
from Lib import datetime

def index(request):
    return render(request, 'blog/index.html', {})

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

            print(title, content, request.user.id, datetime.datetime.now().date())
            post = Post(title = title, content = content, user_id = request.user.id, created_at = datetime.datetime.now().date())
            post.save()

            if post is not None:
                messages.success(request, "Post created successfully")
            else:
                messages.error(request, "An error has been ocurred while trying to create the post")


    return render(request, "blog/create_post.html", context)
