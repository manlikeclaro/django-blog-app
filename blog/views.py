from datetime import date

from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import BlogCommentModelForm
from blog.models import BlogPost, BlogComment


# Create your views here.
def index(request):
    all_blog_posts = BlogPost.objects.all()
    hero_blog_posts = all_blog_posts[:4]
    featured_blog_post = BlogPost.objects.first()

    # Get the latest 3 blog posts
    latest_blog_posts = all_blog_posts.order_by('-date')[:3]

    # Get the oldest 3 blog posts
    oldest_blog_posts = all_blog_posts.order_by('date')[:3]

    context = {'featured': featured_blog_post, 'latest': latest_blog_posts, 'oldest': oldest_blog_posts,
               'hero': hero_blog_posts}
    return render(request, 'blog/index.html', context)


def posts(request):
    all_blog_posts = BlogPost.objects.all()
    # Get the latest blog posts
    latest_blog_posts = all_blog_posts.order_by('-date')

    context = {'posts': latest_blog_posts, }
    return render(request, 'blog/all-posts.html', context)


def single_post(request, slug):
    identified_blog_post = get_object_or_404(BlogPost, slug=slug)
    comments = BlogComment.objects.filter(blog_post=identified_blog_post)

    form = BlogCommentModelForm(request.POST)
    if form.is_valid():
        # form.save()
        comment = form.save(commit=False)
        comment.author = request.user.member
        comment.blog_post = identified_blog_post
        comment.save()
        return redirect('single-post', slug)

    context = {'post': identified_blog_post, 'comments': comments, 'form': form}
    return render(request, 'blog/single-post.html', context)


def about(request):
    return render(request, 'blog/about.html')
