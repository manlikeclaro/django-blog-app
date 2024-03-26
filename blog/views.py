from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return redirect('index')


def index(request):
    return render(request, 'index.html')


def posts(request):
    return render(request, 'all-posts.html')


def single_post(request, single_post):
    return render(request, 'single-post.html')


def about(request):
    return render(request, 'about.html')


