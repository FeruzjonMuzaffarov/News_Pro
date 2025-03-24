from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from news.models import Category, News
from .forms import ProfileUpdateForm
from .forms import UserCreateForm, LoginForm
from django.contrib.auth import login, logout, update_session_auth_hash

from .models import Comment


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreateForm()
    return render(request, 'registration/register.html', {'form': form})


def login_user(request):
    next_url = request.GET.get('next') or request.POST.get('next')  # `next` parametrni olish

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(next_url) if next_url else redirect("profile")  # `next` bo‘lsa, o‘sha sahifaga qaytaradi
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {'form': form})


@login_required
def profile_view(request):
    ctg = Category.objects.all()
    news = News.objects.all().order_by('-date')
    comments = Comment.objects.filter(user=request.user).order_by('-created_at')
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    context = {
        'ctg': ctg,
        'news': news,
        'form': form,
        'comments': comments,
    }

    return render(request, "registration/profile.html", context)


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk, user=request.user)
    comment.delete()
    return redirect('profile')


def logout_user(request):
    logout(request)
    return redirect('index')