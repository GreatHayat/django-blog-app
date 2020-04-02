from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .forms import UserRegisterForm, AddNewPostForm, EditPostForm, UserEditForm, ProfileEditForm, CommentForm
from .models import Category, Post, Profile, Comment, Reply
# Create your views here.


def index(request):
    posts = Post.objects.filter(published=True).order_by('-created_date')
    context = {
        "posts": posts
    }
    return render(request, "crudApp/index.html", context)


def search_posts(request):
    posts = Post.objects.filter(published=True)

    if 'q' in request.POST:
        q = request.POST['q']
        if q:
            searched_posts = posts.filter(Q(category__name__icontains=q) |
                                          Q(post_content__icontains=q) |
                                          Q(title__icontains=q))

    context = {
        "posts": searched_posts
    }
    return render(request, "crudApp/search_posts.html", context)


@login_required(login_url="login")
def profile(request, id):
    profile = get_object_or_404(Profile, id=id, user=request.user)
    posts = Post.objects.filter(
        created_by=request.user).order_by('-created_date')
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(
            request.POST, request.FILES, instance=profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.info(request, "Profile updated successfully!")
            return redirect('profile', id=id)
    else:
        form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)
    context = {
        "profile": profile,
        "posts": posts,
        "form": form,
        "profile_form": profile_form
    }
    return render(request, "crudApp/profile.html", context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    profile = get_object_or_404(Profile, user=post.created_by)
    categories = Category.objects.all()
    context = {
        "post": post,
        "profile": profile,
        "categories": categories
    }
    return render(request, "crudApp/post_detail.html", context)


@login_required(login_url="login")
def add_new_post(request):
    if request.method == "POST":
        form = AddNewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect("dashboard")
    else:
        form = AddNewPostForm()

    context = {
        "form": form
    }
    return render(request, "crudApp/add_new_post.html", context)


@login_required(login_url="login")
def edit_post(request, slug):
    try:
        post = get_object_or_404(Post, slug=slug, created_by=request.user)
    except:
        return redirect('dashboard')

    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, "Post updated successfully!")
            return redirect('dashboard')
    else:
        form = EditPostForm(instance=post)

    context = {
        "form": form
    }
    return render(request, "crudApp/edit_post.html", context)


@login_required(login_url="login")
def delete_post(request, slug):
    try:
        post = get_object_or_404(Post, slug=slug, created_by=request.user)
    except:
        return redirect('dashboard')
    post.delete()
    return


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }
    return render(request, "crudApp/register.html", context)


@login_required(login_url="/login")
def dashboard(request):
    if request.session.has_key('published'):
        msg = request.session['published']
        messages.info(request, msg)
        try:
            del request.session['published']
        except KeyError:
            return HttpResponse("Invalid Key")
    posts = Post.objects.filter(
        created_by=request.user).order_by('-created_date')
    context = {
        "posts": posts
    }
    return render(request, 'crudApp/dashboard.html', context)


@login_required(login_url="login")
def comments(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    replies = Reply.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('comments', id=id)
    else:
        form = CommentForm()
    context = {
        "form": form,
        "comments": comments,
        "replies": replies
    }
    return render(request, "crudApp/comments.html", context)


def test_data(request, id):
    data = dict()
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        data['post'] = "Post Deleted Successfully!"

    return JsonResponse(data)
