from django.shortcuts import render    
from django.http import HttpResponse
from .models import SubRabble, Post, Comment, Like
from django.shortcuts import get_object_or_404, redirect
from .forms import PostForm
from django.contrib.auth.decorators import login_required

## def index(request):
    ##context = {"welcome": "Hello, world!"}

    ##return render(request, "rabble/index.html", context)

def profile(request):
    return render(request, "rabble/profile.html")

def subrabble_list(request):
    if not request.user.is_authenticated:
        return render(request, "rabble/index_anonymous.html")

    subrabbles = SubRabble.objects.all()
    return render(request, "rabble/index.html", {"subrabbles": subrabbles})

@login_required
def subrabble_detail(request, name):
    subrabble = get_object_or_404(SubRabble, name=name)
    posts = Post.objects.filter(subrabble=subrabble)

    for post in posts:
        post.likes_count = Like.objects.filter(post=post).count()
        post.comments_count = Comment.objects.filter(post=post).count()
    
    context = {
        "subrabble": subrabble, 
        "posts": posts
    }

    return render(request, "rabble/subrabble_detail.html", context)

@login_required
def post_detail(request, name, pk):
    subrabble = get_object_or_404(SubRabble, name=name)
    post = get_object_or_404(Post, pk=pk, subrabble=subrabble)
    comments = Comment.objects.filter(post=post)
    likes_count = Like.objects.filter(post=post).count()
    comments_count = comments.count()

    context = {
        "subrabble": subrabble,
        "post": post,
        "comments": comments,
        "likes_count": likes_count,
        "comments_count": comments_count
    }

    return render(request, "rabble/post_detail.html", context)

@login_required
def post_create(request, name):
    subrabble = get_object_or_404(SubRabble, name=name)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.subrabble = subrabble
            post.user = request.user
            post.save()
            return redirect('subrabble-detail', name=subrabble.name)
    else:
        form = PostForm()

    return render(request, 'rabble/post_form.html', {'form': form, 'subrabble': subrabble})

@login_required
def post_edit(request, name, pk):
    post = get_object_or_404(Post, pk=pk)
    subrabble = post.subrabble

    if post.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post since you are not the author!")
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', name=subrabble.name, pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'rabble/post_form.html', {
        'form': form,
        'post': post,
        'subrabble': subrabble
    })
